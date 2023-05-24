function complete_task(task_id) {
    const xhr = new XMLHttpRequest()
    xhr.open(
        "PUT",
        "http://localhost:5000/tasks/complete/" + task_id.toString()
    )
    xhr.send()
}


function set_deadline(task_id, deadline) {
    const xhr = new XMLHttpRequest()
    xhr.open(
        "PUT",
        "http://localhost:5000/deadline/" + task_id.toString() + "/" + deadline.toString()
    )
    xhr.send()
}
