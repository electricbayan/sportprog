function firstpage_request() {
    fetch("/api/task", {
        method: "GET",
        headers: {"task_num": 1,
    "next": "None"}
    })



}