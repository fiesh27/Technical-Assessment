from app import app

from flask import jsonify

from app.models import Divvy



@app.route('/')
def index():
    data = {

        'starttime': Divvy.query.all(),
        'stoptime': Divvy.query.all()
    }
    return jsonify(data)