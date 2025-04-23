from flask import Flask

app = Flask(__name__)
app.secret_key = 'replace_this_later'

from app import routes
