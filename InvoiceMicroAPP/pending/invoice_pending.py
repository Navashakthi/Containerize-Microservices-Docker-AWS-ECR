from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

pendingfile = "invoice_pending.json"
with open(pendingfile, "r") as f:
    pending = json.load(f)

if "chandler" in pending:
    print("YES")

@app.route("/", methods=['GET'])
def hello():
    return ({
        "uri": "/",
        "subresource_uris": {
            "pending": "/pending",
            "pendings": "/pending/<invoice_amount>"
        }
    })

@app.route("/pending/<client_name>", methods=['GET'])
def pending_info(client_name):
    if client_name not in pending:
        raise NotFound

    result = pending[client_name]
    result["uri"] = "/pending/{}".format(client_name)

    return (result)


@app.route("/pending", methods=['GET'])
def pending_record():
    return (pending)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
