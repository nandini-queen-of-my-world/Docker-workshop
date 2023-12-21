from flask import Flask, request, render_template
import os


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        comment = request.form['comment']
        # Store data in a Python variable for now
        data = {
            'name': name,
            'gender': gender,
            'comment': comment
        }
        # Process or store the data here (in-memory for now)
        print(data)
    app_name = os.environ.get("APP_NAME","Simple Flask Form")
    return render_template('index.html',app_name=app_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)
