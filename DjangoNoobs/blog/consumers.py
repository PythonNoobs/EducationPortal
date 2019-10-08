import asyncio
import json
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core import serializers

from .models import Post, Comment


class CommentConsumer(AsyncConsumer):
    """
    Consumer Class for comments based on AsyncConsumer
    """
    async def websocket_connect(self, event):
        """ Method for connect websocket """
        await self.send({
            'type': 'websocket.accept'
        })
        post_id = await self.get_post_id(self.scope['url_route']['kwargs']['slug'])
        # Room name
        self.post = 'post' + post_id
        await self.channel_layer.group_add(
            self.post,
            self.channel_name
        )

    async def websocket_receive(self, event):
        """ Method for receive data from websocket """
        new_comment_data = event.get('text')
        new_comment = json.loads(new_comment_data)
        # Get all fields from front
        post_slug = new_comment['post_slug']
        author = new_comment['user']
        comment_text = new_comment['comment_text']
        parrent_comment = new_comment['parrent_comment']
        # Create comment and return his id
        comment_id = await self.create_comment(post_slug, author, comment_text, parrent_comment)
        comment = Comment.objects.get(id=comment_id)
        # Serialize created comment
        data = serializers.serialize('json', Comment.objects.filter(id=comment_id))
        created_comment = {
            'new_comment': data,
            'parrent_comment': parrent_comment,
            'author': author,
            'get_col': comment.get_col(),
            'get_offset': comment.get_offset(),
            'total_likes': comment.total_likes(),
            'total_dislikes': comment.total_dislikes()
        }
        await self.channel_layer.group_send(
            self.post,
            {
                'type': 'show_comment',
                'text': json.dumps(created_comment) # json.dumps(data) # data
            }
        )

    async def websocket_disconnect(self, event):
        """ Method for disconnect websocket """
        await self.send({
            'type': 'websocket.disconnect'
        })

    @database_sync_to_async
    def create_comment(self, post_slug, author, comment_text, parrent_comment):
        """ Method for create new comment """
        comment = Comment()
        comment.path = []
        comment.post_id = get_object_or_404(Post, slug__iexact=post_slug)
        comment.author_id = User.objects.get(username=author)
        comment.content = comment_text
        comment.save()
        # if this cooment for post, then parrent_comment = ''
        # if this comment for comment, then parrent_coment = int (id parent comment)
        if parrent_comment:
            comment.path.extend(Comment.objects.get(id=parrent_comment).path)
            comment.path.append(comment.id)
        else:
            comment.path.append(comment.id)
        comment.save()
        return comment.id

    @database_sync_to_async
    def get_post_id(self, post_slug):
        """ Method for return post id """
        return str(get_object_or_404(Post, slug__iexact=post_slug).id)

    async def show_comment(self, event):
        """ Method for send comment to front """
        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })