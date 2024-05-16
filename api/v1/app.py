#!/usr/bin/python3

"""
flask app
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close(exception):
    """
    close the storage
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    handle the 404 error page
    """
    response = {"error": "Not found"}
  
if __name__ == "__main__":
  HOST= getenv('HBNB_API_HOST', '0.0.0.0')
  PORT = int(getenv('HBNB_API_PORT', 5000))
  app.run(host=HOST, port=PORT,  threaded=True)
