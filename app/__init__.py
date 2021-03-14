from flask import Flask

app = Flask(__name__)
app.config['N'] = 1

from app import routes
