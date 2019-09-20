from decouple import config
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .models import DB, Record


def create_app():
    app = Flask(__name__) # gives it the name of the module
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = confif('ENV')
    DB.init_app(app)

    @app.route("/")
    def root():
        records = Record.query.all()
        return render_template('base.html', title = 'Home', records=records)

    @app.route('/refresh')
    def refresh():
    # """Pull fresh data from Open AQ and replace existing data."""
        DB.drop_all()
        DB.create_all()
        # TODO Get data from OpenAQ, make Record objects with it, and add to db
        DB.session.commit()
        return render_template('base.html', title='Reset Database!')

    # @app.route('/reset')
    # def reset():
    #     DB.drop_all()
    #     DB.create_all()
    #     return render_template('base.html', title='Reset Database!'

    return app

# if __name__ == '__main__':
#     APP.run(debug=True)