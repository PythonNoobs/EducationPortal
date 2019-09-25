$(document).ready(function(event){
    $(document).on('click', '#like_comment_btn', function(event){
        event.preventDefault();
        var pk = $(this).attr('value');
        var section = "#like-comment-section-" + pk;
        $.ajax({
            type: 'POST',
            url: '{% url "like_comment" %}',
            data: {'comment_id': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
            dataType: 'json',
            success: function(response){
                $(section).html(response['form']);
                console.log($('#like-comment-section').html(response['form']));
            },
            error: function(rs, e){
                console.log(rs.responseText);
            },
        });
    });
});