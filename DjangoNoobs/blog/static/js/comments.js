function show_comments_form(parent_comment_id){
    if (parent_comment_id == 'write_comment'){
        $("#id_parent_comment").val('')
    }
    else{
        $("#id_parent_comment").val(parent_comment_id);
    }
    document.getElementById("comment_button").value = "Ответить";
    document.getElementById("return_comment_button").type = "button";
    document.getElementById("comment_header_text").innerHTML = "Ответить на комментарий";
    var col_offset = document.getElementById("col_offset_comment_" + parent_comment_id).className
    document.getElementById("col_offset_comment_form_container").className = col_offset
    $("#comment_text_form_container").insertAfter("#" + parent_comment_id);
}

function return_comments_form(){
    document.getElementById("comment_button").value = "Комментировать";
    document.getElementById("return_comment_button").type = "hidden";
    document.getElementById("comment_header_text").innerHTML = "Написать комментарий";
    document.getElementById("col_offset_comment_form_container").className = "col mb-2"
    $("#comment_text_form_container").insertAfter("#comment_container");
}