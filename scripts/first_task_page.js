function firstpage_request() {
    fetch('task').then(function (response) {
      return response.text();
    }).then(function(html) {
      window.document.write(html);
    }).catch(function (err) {
      console.warn('err', err)
    })}