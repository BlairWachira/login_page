from flask import Flask,render_template,redirect,request,flash
from models import db,person

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key="blair900"

db.init_app(app)

@app.route("/")
def home():

  return render_template("logging.html")

@app.route("/signin")
def reg():
  if request.method=="POST":
    username=request.form["username"]
    password=request.form["password"]

    user=person(username=username,password=password)
    db.session.add(user)
    db.session.commit()

    flash("user sucessfully regestered","sucessfull")

    redirect("/user_page")

  return render_template("signin.html")

if __name__=="__main__":
  app.run(debug=True)