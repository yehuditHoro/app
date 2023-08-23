
from flask import Flask, render_template, redirect, url_for, request,redirect ,session
import csv
from datetime import datetime
app = Flask(__name__)
room_names = []
app.secret_key = "ABC"

@app.route('/register',methods=['GET','POST'])
def homePage():
    if request.method == 'POST':
        username = request.form['username']
        userpass = request.form['password']
        with open("users.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if username in row:
                  return redirect("/login")          
        data = [[username, userpass]]
        with open("users.csv", "a") as csvfile:
             csvwriter = csv.writer(csvfile)
             csvwriter.writerows(data)
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
     username = request.form['username']
     userpass = request.form['password']
     with open('users.csv', 'r') as users:
         users_arr = csv.reader(users)
         for user in users_arr:
             if user[0] == username:
                 if user[1] != userpass:
                     return "wrong password, try again"
                 else:
                      session['username'] = username
                      return redirect("/lobby")
         return "no such username, try again or register"
    return render_template('login.html')
    

@app.route('/lobby',methods=['GET','POST'])
def lobbyPage():
    if request.method == 'POST':
        new_room = request.form['new_room']
        if new_room not in room_names:
           room_names.append(new_room)
           #room_file = open('./rooms/${room}.txt', 'w') 
           room_file = open(f'./rooms/{new_room}.txt', 'w')  
           room_file.close()
    return render_template('lobby.html',room_names=room_names)

@app.route('/chat/<id>', methods=['GET', 'POST'])
def chat(id):
    return render_template('chat.html', room=id)


@app.route('/api/chat/<id>', methods=['GET', 'POST'])
def update_chat(id):
    if request.method == "POST":
        message = request.form['msg']
        username = session.get('username')  # Use get to avoid errors if username is not set
    
        if not username:
            return "You are not logged in.", 403  # Return a forbidden status code
    
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        with open(f'rooms/{id}.txt', 'a') as file:
            file.write(f'[{timestamp}] {username}: {message}\n')
    
    with open(f'rooms/{id}.txt', 'r') as file:
        all_data = file.read()
    
    return all_data


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000', debug='True')