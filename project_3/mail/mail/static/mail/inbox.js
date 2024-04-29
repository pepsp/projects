document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => compose_email(null));
  document.querySelector('#compose-form').addEventListener('submit', send_email);
  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(reply = null) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#single-email').style.display = 'none';

  // Clear out composition fields

  if(reply){
    document.querySelector('#compose-recipients').value = reply.sender;
    document.querySelector('#compose-subject').value = `Re: ${reply.subject}`;
    document.querySelector('#compose-body').value = `\n----------------------------\n${reply.body}\n`;
    document.querySelector('#compose-body').focus();
    document.querySelector('#compose-body').setSelectionRange(0,0);
  }else{
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  }
}

function send_email(event){
  event.preventDefault();

  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value
  const body = document.querySelector('#compose-body').value;

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => { 
    if(result.error){
      alert(result.error)
    }else{
      alert(result.message);
      const emailsView = document.querySelector('#emails-view');
      emailsView.innerHTML = ''
      load_mailbox('sent');
    }
  });
  
  }

  function single_email(email, mailbox){

    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#single-email').style.display = 'block';
    console.log(email)
    document.querySelector("#single-email").innerHTML = `
    <div class="header">
    <h4> From: </h4><p id="email-from">${email.sender}</p>
    </div>
    <div class="header">
      <h4>To: </h4><p id="email-to">${email.recipients}</p>
    </div>

    <div class="header">
      <h4>Subject: </h4><p id="email-subject">${email.subject}</p>
    </div>

    <div class="header">
      <h4>Timestamp: </h4><p id="email-timestamp">${email.timestamp}</p>
    </div>

    <div id="button-div">
    </div>

      <hr>
    <div id="single-body">
      ${email.body}
    </div>`

    const buttonDiv = document.querySelector("#button-div");

    if(mailbox != 'sent'){
      const archive = document.createElement("button");
      if(email.archived == false){
        archive.innerHTML = 'Archive';
        archive.classList = "btn btn-outline-primary boton"
      }else{
        archive.innerHTML='Unarchive';
        archive.classList="btn btn-outline-danger";
      }

      archive.addEventListener('click', function () {

        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: !email.archived
          })
        })
        .then(() => {load_mailbox('archive')});
     })

      buttonDiv.appendChild(archive);
    }
    
    const reply = document.createElement("button");
    
    reply.innerHTML="Reply";
    reply.classList="btn btn-outline-primary boton";
   
   reply.addEventListener('click', function (){
    compose_email(email);
   });
    
    buttonDiv.appendChild(reply);


  }


function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#single-email').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  console.log(mailbox);

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`)
.then(response => response.json())
.then(emails => {
    x=mailbox;
    console.log(mailbox);
    emails.forEach(email => {
      
    const div = document.createElement('div');

    div.addEventListener('click', function() {
      single_email(email, x);

      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
        
      })
    });

    // HANDLE READ EMAILS LOOK
    if (email.read){
      div.classList.add('email-item', 'read');
    }else{
      div.classList.add('email-item', 'unread')
    }
    ///

    const left = document.createElement('div');
    left.classList.add('left');

    const right = document.createElement('div');
    right.classList.add('right');


    const subject = document.createElement('p');
    subject.textContent = email.subject;
    subject.setAttribute('id', 'subject')

    const sender = document.createElement('p');
    sender.textContent = email.sender;
    sender.setAttribute('id', 'sender');

    const date = document.createElement('p')
    date.textContent = email.timestamp;
    date.setAttribute('id', 'date');

    left.appendChild(sender);
    left.appendChild(subject);
    right.appendChild(date);
    div.appendChild(left);
    div.appendChild(right);

    document.querySelector('#emails-view').appendChild(div)
   });

});
}