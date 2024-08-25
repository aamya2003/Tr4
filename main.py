from flask import Flask



Api = Flask(__name__)



@Api.route("/")
def main():
    return "Hi"



Api.run(host='0.0.0.0', port='8000')
