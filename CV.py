from flask import Flask, render_template, abort, url_for
from projects import projects

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
@app.route("/hem")
def index():
   	return render_template("index.html")


@app.route("/projekt")
def project():
   	return render_template("projects.html", projects=projects)


@app.route("/projekt/<projectTitle>")
def projectPage(projectTitle):
	return render_template("project-site.html", title="project")

	abort(404)



@app.route("/kontakt")
def socials():
   	return render_template("socials.html", title="Sociala Medier")


if __name__ == "__main__":
   	app.run(debug=True, host="0.0.0.0")
   	
