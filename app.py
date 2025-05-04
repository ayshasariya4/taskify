from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

FASTAPI_URL = 'http://127.0.0.1:8000'

@app.route('/')
def index():
    tasks = requests.get(f'{FASTAPI_URL}/tasks').json()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    requests.post(f'{FASTAPI_URL}/tasks', json={'title': title, 'description': description})
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_task(id):
    requests.delete(f'{FASTAPI_URL}/tasks/{id}')
    return redirect('/')

@app.route('/complete/<int:id>')
def complete_task(id):
    tasks = requests.get(f'{FASTAPI_URL}/tasks').json()
    task = next((t for t in tasks if t['id'] == id), None)
    if task:
        updated_task = {
            'title': task['title'],
            'description': task['description'],
            'status': 'Completed'
        }
        requests.put(f'{FASTAPI_URL}/tasks/{id}', json=updated_task)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
