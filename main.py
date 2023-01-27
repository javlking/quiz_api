from flask import Flask
import api

app = Flask(__name__)

app.register_blueprint(api.bp)


@app.get('/')
def home():
    return {'text': 'Hello world'}


app.run()

