const login = localStorage.getItem('username');

let page_login = document.getElementById('enter_account');


if (String(login) == 'null') {
    page_login.textContent = 'Войти в аккаунт';
}
else {
    page_login.textContent = login
}


const changeText = () => {
    // Выбираем элемент на странице, и меняем содержимое нужного поля
    document.getElementsByClassName('enter_account')[0].textContent = login;
  }
  