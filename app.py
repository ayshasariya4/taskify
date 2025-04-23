from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Frontend route to display tasks
@app.route('/')
def index():
    tasks = requests.get('http://127.0.0.1:8000/tasks').json()  # Fetch tasks from FastAPI
    return render_template('index.html', tasks=tasks)

# Frontend route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    requests.post('http://127.0.0.1:8000/tasks', json={'title': title, 'description': description})
    return redirect('/')

# Frontend route to delete a task
@app.route('/delete/<int:id>')
def delete_task(id):
    requests.delete(f'http://127.0.0.1:8000/tasks/{id}')
    return redirect('/')

@app.route('/complete/<int:id>')
def complete_task(id):
    # Send PUT request to FastAPI backend to update the task's status
    response = requests.put(f'http://127.0.0.1:8000/tasks/{id}', json={'status': 'Completed'})
    print(response.json())  # This will print the response for debugging
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
