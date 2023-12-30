from flask import Flask, redirect, request, url_for, render_template
import sqlite3

app = Flask(__name__)

@app.route("/loginsuccess")
def loginsuccess():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def login():
    if request.method == "POST":
        print("")
        username = request.form['username']
        password = request.form['password']
        count = userLogin(username, password)
        
        if count is None:
            return redirect(url_for('loginfailed'))
        return redirect(url_for('loginsuccess'))
    else:
        pass

def userLogin(x, y):
    connection = sqlite3.connect("login.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT username, password FROM account WHERE username = ? AND password = ?;", (x, y))
    count = cursor.fetchone()
    
    connection.close()
    return count

if __name__ == "__main__":
    app.run(debug=True)