from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    task = request.form.get('task')
    if task in tasks:
        tasks.remove(task)
    return redirect('/')

if __name__ == 'main':
    app.run(debug=True,port=5001)