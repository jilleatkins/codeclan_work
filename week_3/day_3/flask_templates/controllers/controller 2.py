from app import app
from flask import render_template, request
from models.todo_list import tasks
from models.task import Task

@app.route('/tasks')
def show_tasks():
    return render_template('index.html', title ="Home", tasks=tasks)

@app.route('/tasks/<int:task_id>')
def show_task(task_id):
    task = tasks[task_id]
    return render_template('task.html', task=task)

@app.route('/tasks', methods=['POST'])
def add_task():
    form_data = request.form
    title = form_data['title']
    description = form_data['description']
    new_task = Task(title, description, False)
    tasks.append(new_task)
    return "Task added"
