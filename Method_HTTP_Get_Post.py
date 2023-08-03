# BACK END
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__) 
@app.route('/') 
def home(): 
	return render_template("child_template.html") 



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route('/<usr>') 
def user(usr): 
	return f'<h1> {usr} </h1>' 


if __name__=="__main__":
	app.run(debug=True) # It allows us not to rerun the server every time we make a change