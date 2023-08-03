from flask import Flask, redirect, url_for, render_template


app = Flask(__name__) 

@app.route('/') 
def home(): 
	return render_template("child_template.html", content="Testing") #render_template fonction parametrée qui permet d'afficher la page html avec

@app.route('/test') 
def test(): 
	return render_template("empty.html") #adding an empty app, the navbar is still there


if __name__=="__main__":
	app.run(debug=True) # It allows us not to rerun the server every time we make a change