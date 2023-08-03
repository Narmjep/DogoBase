from flask import Flask, render_template
import api

app = Flask(__name__)

@app.route('/')
def index():
    return api.get_random_name()

@app.route('/male')
def male():
    return api.get_random_male()

@app.route('/female')
def female():
    return api.get_random_female()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)