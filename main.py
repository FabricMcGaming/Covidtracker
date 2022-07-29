from flask import *


# creates flask app
app = Flask('Covidtracker')

#decorator to say: this route will return this function
@app.route('/')
def main():
    return render_template('main.html')


# runs app
app.run()