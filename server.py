from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/learn_more.html")
def learn_more():
    return render_template('learn_more.html')

if __name__ == "__main__":
    app.run(debug=True)