from flask import *
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("content.html")

if __name__ == "__main__":
    app.run("0.0.0.0")