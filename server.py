from flask import Flask, render_template, request,redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users_list():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read.html",users_list=users)

@app.route('/users/new')
def create_user():
            
    return render_template("create.html")

@app.route("/new",methods=['POST'])
def new_user():
    
    print(request.form)
    User.save(request.form)
    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)

