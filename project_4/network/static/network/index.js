document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views

    document.querySelector('#compose-post').addEventListener('click', () => showPost());

    
    
  });


function showPost(){
    let post = document.querySelector('#show-post');

    if (post.style.display === "none" || post.style.display === ""){
        post.style.display = 'block';
        document.querySelector('#post-text').focus()
    }else{
        post.style.display = 'none';
    }
}