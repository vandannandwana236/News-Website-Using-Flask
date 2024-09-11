from flask import Flask,render_template,request
import requests
app = Flask(__name__)
app.secret_key = "vandan"

@app.route("/")
def index():
    get_api = "https://newsapi.org/v2/top-headlines?country=us&apiKey=adb6aaba259640ca85ee6ab4a9d83074"
    r = requests.get(get_api).json()
    case = {
        'articles':r['articles']
    }
    return render_template('index.html',cases = case)

@app.route("/science")
def science():
    get_api = "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=adb6aaba259640ca85ee6ab4a9d83074"
    r = requests.get(get_api).json()
    case = {
        'articles':r['articles']
    }
    return render_template('science.html',cases = case)


if __name__ == '__main__':
    app.run(debug=True)