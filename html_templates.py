from flask import Flask, redirect, url_for, render_template
# copier coller l'URL qui est dans la console sur le navigateur
#{% ....... %} permet d'écrire en python sur un code  HTML
# enregistrer le fichier python et le fichier HTML dans le meme dossier sinon ça ne fonctionne pas

app = Flask(__name__) 

@app.route('/<name>') 
def home(name): 
	return render_template("index.html", content=name,r=2) #render_template fonction parametrée qui permet d'afficher la page html avec


@app.route('/list') 
def list():  
	return render_template("index.html", var=["tim","joe","bill"])
# ce qu'il y a dans list n'apparait pas dans home, mais ce qu'il y a dans home apparait dans list, il est inclu à la page html

if __name__=="__main__":
	app.run() 