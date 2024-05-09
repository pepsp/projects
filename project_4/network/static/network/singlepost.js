document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#open-comment').addEventListener('click', () => showComment())
    
    
  });
function showComment(){
    let comment = document.querySelector('#show-comment');
    console.log(comment.style.display);
    if (comment.style.display === "none" || comment.style.display === ""){
        comment.style.display = 'block';
        document.querySelector('#post-comment').focus()
    }else{
        comment.style.display = 'none';
    }
}