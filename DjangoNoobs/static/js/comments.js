function show_comments_form(parent_comment_id)
{
    if (parent_comment_id == 'write_comment')
    {
        $("#id_parent_comment").val('')
    }
    else
    {
        $("#id_parent_comment").val(parent_comment_id);
    }
    $("#comment_form").insertAfter("#" + parent_comment_id);
}