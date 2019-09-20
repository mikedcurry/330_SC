from decouple import config
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .models import DB, Record
from .pull_api import get_values, unity
# from .openaq_py import *


def create_app():
    app = Flask(__name__) # gives it the name of the module
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = config('ENV')
    DB.init_app(app)

    @app.route("/")
    def root():
        records = Record.query(Record.value>=10).all()
        return render_template('base.html', title = 'Home', records=records)

    @app.route('/update')
    def refresh():
    # update data from API
        DB.drop_all()
        DB.create_all()
        for thing in get_values(city='Los Angeles', parameter='pm25'):
            records = Record(datetime=str(thing[0]), value=thing[1])
            DB.session.add(record)
        DB.session.commit()
        return render_template('update.html', title='Reset Database!')


    return app



# if __name__ == '__main__':
#     APP.run(debug=True)