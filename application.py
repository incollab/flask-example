from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'This is awesome! What are you view is greatest'
