// REGISTER USER
async function registerUser(){

let email = document.getElementById("email").value
let password = document.getElementById("password").value

let res = await fetch("/register",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
email:email,
password:password
})
})

let data = await res.json()

alert(data.message)

window.location.href="/login-page"

}



// LOGIN USER
async function loginUser(){

let email = document.getElementById("email").value
let password = document.getElementById("password").value

let res = await fetch("/login",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
email:email,
password:password
})
})

let data = await res.json()

if(data.access_token){

localStorage.setItem("token",data.access_token)

alert("Login Successful")

window.location.href="/tasks-page"

}else{

alert("Login Failed")

}

}



// ADD TASK
async function addTask(){

let title = document.getElementById("taskTitle").value

if(title === ""){
alert("Enter a task")
return
}

let res = await fetch("/tasks",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
title:title
})
})

await res.json()

document.getElementById("taskTitle").value=""

loadTasks()

}



// LOAD TASKS
async function loadTasks(){

let res = await fetch("/tasks")

let tasks = await res.json()

let list = document.getElementById("taskList")

list.innerHTML=""

tasks.forEach(task=>{

let li = document.createElement("li")

li.innerHTML = `
<span class="${task.completed ? 'completed' : ''}">
${task.title} - ${task.completed ? "Completed" : "Pending"}
</span>

<div>

${!task.completed ? 
`<button class="complete" onclick="completeTask(${task.id})">Complete</button>` 
: ""}

<button class="delete" onclick="deleteTask(${task.id})">Delete</button>

</div>
`

list.appendChild(li)

})

}



// COMPLETE TASK
async function completeTask(id){

await fetch(`/tasks/${id}`,{
method:"PUT"
})

alert("Task Completed")

loadTasks()

}



// DELETE TASK
async function deleteTask(id){

await fetch(`/tasks/${id}`,{
method:"DELETE"
})

alert("Task Deleted")

loadTasks()

}