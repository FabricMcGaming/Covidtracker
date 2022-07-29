from flask import *


app = Flask('Covidtracker')

@app.route('/')
def main():
    return render_template('main.html')


app.run()