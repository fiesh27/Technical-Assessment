from app import app, db

from app.models import Divvy



@app.shell_context_processor
def make_context():
    return {'db': db, 'Divvy': Divvy}