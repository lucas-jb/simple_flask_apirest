import argparse
#App
from app import create_app
from flask import jsonify

app = create_app()

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello world!"})


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong!"})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='Activates debug mode, require value port', action="store_true" , required=False)
    parser.add_argument('-p', help='Port number for the webservice', type=int, default=80, required=False)
    args = parser.parse_args()
    app.run(debug=args.d, port=args.p)