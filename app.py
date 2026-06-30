from flask import Flask, render_template, request
import json

app = Flask(__name__)


def load_movies():
    with open("data/movies.json", "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/movies")
def movies():

    keyword = request.args.get("keyword", "").strip()

    movies = load_movies()

    if keyword != "":
        movies = [
            movie for movie in movies
            if keyword.lower() in movie["title"].lower()
            or keyword.lower() in movie["genre"].lower()
            or keyword.lower() in movie["review"].lower()
        ]

    return render_template(
        "movies.html",
        movies=movies,
        keyword=keyword
    )


if __name__ == "__main__":
    app.run(debug=True)