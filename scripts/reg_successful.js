let username = document.head.querySelector("[id~=username][content]").content;
let email = document.head.querySelector("[id~=email][content]").content;

localStorage.setItem('username', username)
localStorage.setItem('email', email)