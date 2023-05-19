from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="172.31.12.23",
    user="sandip",
    password="Sandip@1997",
    database="pythonlogin"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Insert user data into the database
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
