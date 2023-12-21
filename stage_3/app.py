from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import logging
import os
import socket

app = Flask(__name__)

# Configure Flask to use PostgreSQL as the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db:5432/mydatabase'
db = SQLAlchemy(app)

# Define the 'data' table using SQLAlchemy
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    text = db.Column(db.Text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        text = request.form['text']

        # Create a new Data object and insert it into the database
        new_data = Data(name=name, gender=gender, text=text)
        db.session.add(new_data)
        db.session.commit()

        logging.info(f'Data inserted into the "data" table with ID: {new_data.id}')
    

    
    all_data = Data.query.all()
    app_name = os.environ.get("APP_NAME")
    hostname = socket.gethostname()
    return render_template('index.html', all_data=all_data,app_name=app_name,hostname=hostname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
