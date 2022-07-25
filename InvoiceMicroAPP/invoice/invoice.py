from flask import Flask
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

invoicefile = "invoice.json"
with open(invoicefile, "r") as f:
    invoices = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    return ({
        "uri": "/",
        "subresource_uris": {
            "invoice": "/invoice",
            "invoices": "/invoices/Invoice_Number"
        }
    })


@app.route("/invoice", methods=['GET'])
def invoice_list():
    return (invoices)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
