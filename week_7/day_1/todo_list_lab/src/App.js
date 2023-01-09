import React, { useState } from 'react';
import './App.css';

function App() {

  const [taskList, setTaskList] = useState([
    { name: "Buy shopping", priority: "Low", isCompleted: false },
    { name: "Clean bathroom", priority: "Low", isCompleted: true },
    { name: "Shave armpits", priority: "High", isCompleted: false },
  ])


  const [taskName, setTaskName] = useState("")
  const [priority, setPriority] = useState("")

  const nodeList = taskList.map((task, index) => <li key={index} className={task.priority}> {task.name}</li>)

  const handleTaskInput = (event) => {
    setTaskName(event.target.value)
  }

  const handlePrioritySelect = (event) => {
    setPriority(event.target.value)
  }

  const taskNodes = taskList.map((task, index) => {
    return <li key={index} className={task.isCompleted ? "completed" : "not-completed"}>
      <span>{task.name}</span>
      {task.priority ?
      <span priority="High">Priority: High</span> : <span priority="Low" >Priority: </span>}
      {task.isCompleted ?
        <span className="completed">Completed</span> : <button onClick={() => completeTask(index)}>Complete</button>}
    </li>
  })

  const saveNewTask = (event) => {
    event.preventDefault();
    const taskListCopy = [...taskList]
    taskListCopy.push({ name: setTaskName, priority: priority, isCompleted: false })
    setTaskList(taskListCopy)
    setTaskName("")
    setPriority("")
  }

  const completeTask = (index) => {
    const taskListCopy = [...taskList]
    const updatedTask = { ...taskListCopy[index] }
    updatedTask.isCompleted = true
    taskListCopy[index] = updatedTask
    setTaskName(taskListCopy)
  }

  

  return (
    <div className="App">

      <h1>To-Do List</h1>
      <hr></hr>

      <form onSubmit={saveNewTask}>
        <label htmlFor="new-todo">Add a new todo:</label>
        <input id="new-task" type="text" placeholder="e.g. Vacuum living room" value={setTaskName} onChange={handleTaskInput} />
        <label>Task priority: </label>
        <label htmlFor="high">High</label>
        <input id="high" type="radio" checked={priority === "high"}name="prioritySelect" value="high" onChange={handlePrioritySelect} />
        <label htmlFor="low">Low</label>
        <input id="low" type="radio" name="prioritySelect" value="low" onChange={handlePrioritySelect} checked={priority === "low"}/> 
        <input type="submit" value="Save new task" />
      </form>

      <ul>
        {nodeList}
      </ul>



    </div>
  );
}

export default App;
