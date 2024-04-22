function sendRequest(body=null) {
  return new Promise( (resolve, reject) => {
      const xhr = new XMLHttpRequest();

      xhr.open('POST', '/api/post_task');

      xhr.setRequestHeader('Content-Type', 'application/json')

      xhr.responseType = 'json';
      xhr.onload = () => {
          if (xhr.status < 400) {
          resolve(xhr.response) }
          else {
              reject(xhr.response)
          }
      }

      xhr.send(JSON.stringify(body));
  })
}


function post_solution() {
sendRequest({
  solution: document.getElementById('solutioncontent').textContent,
  nickname: ''
  }).then(data =>console.log(data)).catch(err => console.log(err))

  if (data['status'] == 'OK') {
    document.getElementById('verdict').textContent = 'OK'
  }
  else {
    document.getElementById('verdict').textContent = 'WA'
  }
}