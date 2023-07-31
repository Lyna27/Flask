from flask import Flask, redirect, url_for

# copier coller l'URL qui est dans la console sur le navigateur


app = Flask(__name__) # instance of a flask web application

@app.route('/') #adding a root with a path "/" that means that page, so that flask knows where the page is going
def home():  #Creating a page called home
	return "Hello this is the main page <h1>Hello</h1>" #HTML fonctionne meme en codant en python !

#creating another app
@app.route("/<name>") #en ajoutant /... à l'URL on obtiendra Hello ... ! ; <name> est un parametre
def user(name):
	return f"Hello {name} !" #f"" permet d'ecrire en string tout avec la possibilié d'ajouter les variables

@app.route("/admin")
def admin():
	return redirect(url_for("home")) #it redirect us to the home page 
	#Now whenever we visit "https.../admin" we will be redirected home

@app.route("/help")
def help():
	return redirect(url_for("user", name="I'm learning how to use Flask"))
	#Whenever we visit "https.../help" we will be redirected to the user page, with name ="..." as a parameter

if __name__=="__main__":
	app.run() #running the app
