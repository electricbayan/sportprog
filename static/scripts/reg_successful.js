let nickname = document.head.querySelector("[id~=username][content]").content;
let email = document.head.querySelector("[id~=email][content]").content;

localStorage.setItem('nickname', nickname)
localStorage.setItem('email', email)
