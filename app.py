import os
from flask import Flask, render_template, request, redirect, url_for
#from datetime import date
import psycopg2

app = Flask(__name__)

DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')

def database_connect():
    return psycopg2.connect(database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST)

def get_next_task_id():
    connection = database_connect()
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(id) FROM tasks")
    max_id = cursor.fetchone()[0] # first find in row and first column
    connection.close()
    return max_id + 1 if max_id else 1

@app.route("/")
def index():
    feedback_message = request.args.get('feedback_message') #  Get the message from URL parametres
    connection = database_connect()
    cursor = connection.cursor()

    # Získanie úloh pre každý stĺpec
    cursor.execute("SELECT * FROM tasks WHERE status = 'todo'")
    todo_tasks = cursor.fetchall()

    cursor.execute("SELECT * FROM tasks WHERE status = 'doing'")
    doing_tasks = cursor.fetchall()

    cursor.execute("SELECT * FROM tasks WHERE status = 'done'")
    done_tasks = cursor.fetchall()

    connection.close()

    return render_template('tasks.html', todo_tasks=todo_tasks, doing_tasks=doing_tasks, done_tasks=done_tasks, feedback_message=feedback_message)

@app.route("/add_task", methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    status = 'todo'  # Default status for a new task

    connection = database_connect()
    cursor = connection.cursor()

    # Check if the task already exists
    cursor.execute("SELECT id FROM tasks WHERE task = %s", (task_name,))
    existing_task = cursor.fetchone()

    if existing_task:
        # If the task already exists, do not add it again
        feedback_message = "Task already exists."
    else:
        # If the task doesn't exist, add it to the database
        task_id = get_next_task_id()
        cursor.execute("INSERT INTO tasks (id, task, status) VALUES (%s, %s, %s)", (task_id, task_name, status))
        connection.commit()
        feedback_message = "Task added successfully."

    connection.close()

    return redirect(url_for('index', feedback_message=feedback_message))

@app.route("/move_task", methods=['POST'])
def move_task():
    task_id = request.form['task_id']
    target_status = request.form['status']

    connection = database_connect()
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (target_status, task_id))
    connection.commit()
    connection.close()

    return redirect(url_for('index'))

@app.route("/delete_task", methods=['POST'])
def delete_task():
    task_id = request.form['task_id']

    connection = database_connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    connection.commit()
    connection.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
