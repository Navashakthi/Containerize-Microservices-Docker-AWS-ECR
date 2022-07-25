from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

paidfile = "./invoice_processed.json"
with open(paidfile, "r") as f:
    processed = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    return ({
        "uri": "/",
        "subresource_uris": {
            "processed": "/processed",
            "process": "/processed/<date>"
        }
    })


@app.route("/processed", methods=['GET'])
def processed_list():
    return (processed)


@app.route("/processed/<date>", methods=['GET'])
def processed_record(date):
    if date not in processed:
        raise NotFound
    return (processed[date])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5003")