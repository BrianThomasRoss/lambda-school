from openaq import API, OpenAQ
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from dotenv import load_dotenv
from .models import DB, City, Record

load_dotenv()
api = OpenAQ()

def create_app():
    APP = Flask(__name__)
    api = OpenAQ()
    APP.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    DB.init_app(APP)

    @APP.route('/')
    def root():
        """Base view."""
        city_list = [('Los Angeles',1),('Mainz',2)]
        return render_template('home.html', 
                                city_list=city_list,
                                title='Air Quality Monitor')


    @APP.route('/refresh')
    def refresh():        
        DB.drop_all()
        DB.create_all()
        city_list = ['Los Angeles','Mainz']
        
        for name in city_list:
            db_city=City(name=name)

            for x in times_and_values(city=db_city.name):
                db_record = Record(datetime=x[0], value=x[1])
                db_city.records.append(db_record)
                DB.session.add(db_record)
        
        DB.session.commit()
        return 'Refreshed!'

    @APP.route('/city/<city_id>', methods=['GET'])
    def city(city_id=None):
        city_id = city_id
        above10 = Record.query.filter(Record.value > 10).all()
        this_city = City.query.filter(City.id == city_id).one()
        return render_template('city.html', 
                                above10=above10, 
                                this_city=this_city)

    return APP


def times_and_values(city='Los Angeles', parameter='pm25'):
    status, body = api.measurements(city=city, parameter=parameter)
    results = []
    for row in body['results']:
        date = row['date']['utc']
        value = row['value']
        results.append((date, value))
    return results

