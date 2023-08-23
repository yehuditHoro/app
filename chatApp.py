from flask import Flask, render_template, redirect, url_for, request,redirect
import csv,os

app = Flask(__name__)


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




@app.route('/login', methods=['GET','POST'])
def loginPage():
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
                      return redirect("/lobby")
             return "no such username, try again or register"
    return render_template('login.html')
    

# @app.route('/lobby',methods=['GET','POST'])
# def lobbyPage():
#     if request.method == 'POST':
#         new_room = request.form['new_room']
#         if new_room not in os.listdir("./rooms"):
#            room_file = open('./rooms/${room}.txt', 'w') 
#     return render_template('lobby.html')
  
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000', debug='True')