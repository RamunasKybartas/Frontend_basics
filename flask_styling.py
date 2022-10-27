from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/styling/home.html")

@app.route("/news")
def news():
    return render_template("/styling/news.html")

@app.route("/edits")
def edits():
    return render_template("/styling/edits.html")

@app.route("/stuff")
def stuff():
    return render_template("/styling/stuff.html")

@app.route("/containers")
def containers():
    return render_template("/styling/containers.html")

@app.route("/grid")
def grid():
    return render_template("/styling/grid.html")

@app.route("/page")
def page():
    return render_template("/styling/fullpage.html")

if __name__ == "__main__":
    app.run(debug=True)
