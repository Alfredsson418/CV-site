from flask import Flask, render_template, abort, url_for

app = Flask(__name__)


projects = [
	{
	   'title': 'Morse Code Translator',
	   'p': 'A python script to translate morse code',
	   'color': 'rgb(75, 127, 255)',
	   'done' : 'Fullbordad'
	},
		{
	   'title': 'Websida',
	   'p': 'Backend och Frontend',
	   'color': 'rgb(75, 100, 200)',
	   'done' : 'Inte Startad'
	},
	{
		'title': 'Test',
		'p': 'Information',
		'color': 'tomato',
		'done': 'Nej'
	
	}
]




@app.route("/")
@app.route("/hem")
def index():
   	return render_template("index.html")


@app.route("/projekt")
def project():
   	return render_template("project.html", title="Projekt", projects=projects)


@app.route("/projekt/<projectTitle>")
def projectPage(projectTitle):
	for project in projects:
		if projectTitle == project.get("title"):
			return render_template("projectTemp.html", project=project)

	abort(404)

@app.route("/sociala-medier")
def socials():

   	return render_template("socials.html", title="Sociala Medier")


if __name__ == "__main__":
   	app.run(debug=True, host="0.0.0.0")
   	
