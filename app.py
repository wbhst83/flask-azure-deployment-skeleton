from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world on Azure!</h1>'

if __name__ == '__main__':
    os.environ.setdefault('Flask_SETTINGS_MODULE', 'helloworld.settings')
    app.run(debug=True)

