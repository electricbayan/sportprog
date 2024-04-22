function next_task() {

    let task_num = document.head.querySelector("[id~=task_num][content]").content;
    fetch("/api/task", {
        method: "GET",
        headers: {"task_num": task_num,
        "next": Number(task_num) + 1}
    })
}

function prev_task() {
    let task_num = document.head.querySelector("[id~=task_num][content]").content;
    fetch("/api/task", {
        method: "GET",
        headers: {"task_num": task_num,
        "next": Number(task_num) - 1}
    })

}
