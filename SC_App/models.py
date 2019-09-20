#  models mean schema in web speak....
from flask_sqlalchemy import SQLAlchemy

# APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

DB = SQLAlchemy()


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(50))
    value = DB.Column(DB.Float, nullable=False)
    def __repr__(self):
        return "(Datetime %r, Value %r)" %(self.datetime, self.value)
        # 'TODO - write a nice representation of Records'
        







# DB = SQLAlchemy()


# #create class that makes a table in DB
# class <Table_Name>(DB.Model):
#     id = DB.Column(DB.Integer, primary_key=True) # going to need this key column...
#     <name> = DB.Column(DB.String(15), nullable=False)
#     <newest_tweet_id> = DB.Column(DB.BigInteger)
#     def __repr__(self):
#         return '<User {}>'.format(self.<name>)