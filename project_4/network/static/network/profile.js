document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views

    document.querySelectorAll(".like-button").forEach(button => {
        button.addEventListener('click', function(){
            likeHandler(button.dataset.post, button.dataset.liked);
        });
    })
    
    
  });

function likeHandler(post, liked){
    const likeButton = document.getElementById(`boton-${post}`);
    const contador = document.getElementById(`contador-${post}`)
    let valorContador = contador.innerHTML;

if(liked === 'true'){
    fetch(`/unlike/${post}`)
    .then(response => {
        if (response.ok) {
            // If response is successful, handle it
            let icono = document.getElementById(`icon-${post}`);
            icono.classList.remove('liked');
            likeButton.setAttribute('data-liked','false')
            valorContador--;
            contador.innerHTML= valorContador;
            console.log("Post unliked successfully");
        } else {
            // If response is not successful, handle error
            console.error("Failed to unlike post");
        }
    })
} else if(liked === 'false'){
    fetch(`/like/${post}`)
    .then(response => {
        if (response.ok) {
            // If response is successful, handle it
            let icono = document.getElementById(`icon-${post}`);
            icono.classList.add('liked');
            likeButton.setAttribute('data-liked','true')
            valorContador++;
            contador.innerHTML= valorContador;
            console.log("Post liked successfully");
        } else {
            // If response is not successful, handle error
            console.error("Failed to like post");
        }
    })
}
}