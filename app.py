from flask import *
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/background")
def background():
    return render_template("background.html")

@app.route("/skill")
def skill():
    return render_template("skill.html")

if __name__ == "__main__":
    app.run("0.0.0.0")