from flask import Flask,render_template,redirect,request,flash,url_for,session
from models import db,person

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key="blair900"

db.init_app(app)

@app.route("/", methods=["POST","GET"])
def login():
  if request.method=="POST":
     username=request.form["username"]
     password=request.form["password"]

     user=person.query.filter_by(username=username).first()

     if not user:
        flash("user do not exists","error")
        return redirect(url_for("login"))
     
     if user.password != password:
        flash("incorrect password","error")
        return redirect(url_for("login"))
     
     session["user_id"]=user.id
     session["username"]=user.username

     return redirect(url_for("userpage"))
  
  return render_template("logging.html")

@app.route("/signin", methods=["POST","GET"])
def signin():
  if request.method=="POST":
    username=request.form["username"]
    password=request.form["password"]

    exist_user=person.query.filter_by(username=username).first()
    if exist_user:
      print("username exists")
      flash("username already exists","error")
      return redirect(url_for("signin"))

    user=person(username=username,password=password)
    db.session.add(user)
    db.session.commit()

    flash("user sucessfully regestered","sucess")

    return redirect(url_for("userpage"))

  return render_template("signin.html")

@app.route("/userpage")
def userpage():
    # Get username from session
    username = session.get("username")

    if username is None:
        flash("Please log in first", "error")
        return redirect(url_for("login"))
    return render_template("user_page.html", username=username)



if __name__=="__main__":
  with app.app_context():
        db.create_all()
  app.run(debug=True)