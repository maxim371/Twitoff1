''' main application and routing doc for twitoff.'''

#from decouple import config
from flask import Flask, render_template, request
from .models import DB, User


#make our app factory

def create_app():
    app = Flask(__name__)

    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #have the database know the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    return app