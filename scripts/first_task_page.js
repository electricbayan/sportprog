function firstpage_request() {
    alert(1)
    fetch("http://127.0.0.1:5000/api/task", {
        method: "GET",
        headers: {"task_num": 1,
    "next": "None"}
    });



}