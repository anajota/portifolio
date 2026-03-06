from flask import Flask, render_template
import requests

app = Flask(__name__)

GITHUB_USER = "anajota"

def get_repos():
    url = f"https://api.github.com/users/{GITHUB_USER}/repos"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return []

@app.route("/")
def home():

    repos = get_repos()

    return render_template("index.html", repos=repos)


if __name__ == "__main__":
    app.run(debug=True)