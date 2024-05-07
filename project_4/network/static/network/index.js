document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#compose-post').addEventListener('click', () => showPost());
  });

function showPost(){
    let post = document.querySelector('#show-post');
    console.log(post.style.display)
    if (post.style.display === "none" || post.style.display === ""){
        post.style.display = 'block';
        document.querySelector('#comment').focus()
    }else{
        post.style.display = 'none';
    }
}