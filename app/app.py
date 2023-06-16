from flask import Flask,render_template,jsonify
from movies import movies
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies_get_all():
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
