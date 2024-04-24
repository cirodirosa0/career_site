from flask import Flask, render_template, Response, request
from testing import Testing

app = Flask(__name__)
test_source = Testing()


@app.route("/")
@app.route("/index.html")
def home():
    return render_template('index.html')


@app.route("/learn_more.html")
def learn_more():
    return render_template('learn_more.html')


@app.route('/plot.png')
def plot():
    threshold = request.args.get('threshold', default=0.1, type=float)
    img = test_source.plot_me(threshold)
    return Response(img.getvalue(), mimetype='image/png')

@app.route('/update_plot')
def update_plot():
    threshold = request.args.get('threshold', default=0.1, type=float)
    img = test_source.plot_me(threshold)
    return Response(img.getvalue(), mimetype='image/png')

@app.route("/testing.html")
def test():
    return render_template('testing.html')


if __name__ == "__main__":
    app.run(debug=True)
