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

if __name__ == "__main__":
    app.run(debug=True)
