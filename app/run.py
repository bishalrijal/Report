from flask import  render_template, jsonify
from flask_restful import Resource, Api
import mainapp.scheduler as scheduler
import mysql.connector
from app import app
from database import connection
import pandas as pd
import json
from flask_cors import CORS

CORS(app, supports_credentials=True)
api = Api(app)
class UserData(Resource):
    def get(self):
        file = pd.read_csv('new.csv')
        df = pd.DataFrame(file)
        df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%m-%d')
        df['count'] = df['is_active']
        df = df[['created_at','count']]
        df = df.groupby(['created_at']).count()
        df = df.to_dict()        
        return jsonify(df)

api.add_resource(UserData, '/getdata')

@app.route('/')
def index():
    from utils.menu import menu
    return render_template('sidebar.html',menu = menu)


if __name__ == '__main__':
    scheduler.cron_job()
    app.run(debug=False)
    