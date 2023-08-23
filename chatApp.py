from flask import Flask, render_template, redirect, url_for, request,redirect
import csv

app = Flask(__name__)

import re
@app.route('/register',methods=['GET','POST'])
def homePage():
    if request.method == 'POST':
        username = request.form['username']
        userpass = request.form['password']
        username = re.sub(r"[^\w\s]", "", username)
        with open("users.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
        for row in csvreader:
            if username in row:
                return redirect("/login") 
        csvfile.close()          
        data = [[username, userpass]]
        with open("users.csv", "a") as csvfile:
             csvwriter = csv.writer(csvfile)
             csvwriter.writerows(data)
             csvfile.close()
        
    return render_template('register.html')

@app.route('/login')
def loginPage():
    return "kk"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000', debug='True')


# from flask import Flask, render_template, redirect, url_for, request

# app = Flask(__name__)

# def handling_request_register():
#     if request.method == 'POST':
#         name = request.form['username']
#         password = request.form['password']
#         return f"data from user: Name - {name}, password - {password}"
#     return render_template('register.html')

# def handling_request_login():
#     if request.method == 'POST':
#         name = request.form['username']
#         password = request.form['password']
#         return f"data from user: Name - {name}, password - {password}"
#     return render_template('login.html')

# def handling_request_lobby():
#     return render_template('lobby.html')
#     # new_room=

# @app.route('/', methods=['GET', 'POST'])
# def homePage():
#     return handling_request_register()

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     return handling_request_register()

# @app.route('/login', methods=['GET', 'POST'])
# def loginPage():
#     return handling_request_login()

# @app.route('/lobby', methods=['GET', 'POST'])
# def lobby():
#     return handling_request_lobby()

# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0', port='5000', debug='True')
