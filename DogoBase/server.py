from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from api import *
from database import *

# Setup
app = Flask(__name__)


# Home page
@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    api.init_app(app)
    dbPath = __file__ + '/../database.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbPath
    db.init_app(app)
    with app.app_context():
        print("creating database")
        db.create_all()
    print(api.resources)
    app.run(debug=True)
