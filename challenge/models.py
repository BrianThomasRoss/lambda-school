from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)
    city_id = DB.Column(DB.Integer, DB.ForeignKey('city.id'), nullable=False)
    city = DB.relationship('City', backref=DB.backref('records', lazy=True))

    def __repr__(self):
        return '< Time {} --- Value {} >'.format(self.datetime, self.value)


class City(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(25), nullable=False)

    def __repr__(self):
        return '< {} --- {} >'.format(self.id, self.name)