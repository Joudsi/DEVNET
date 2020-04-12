"""
Simple flask web app that demonstrates the Model View Controller
(MVC) pattern in meaningful and somewhat realistic way.
"""

from flask import Flask, render_template, request
from database import Database

# Create Flask object and instantiate database object
app = Flask(__name__)

# path = "data/db.json"
# path = "data/db.yml"
path = "data/db.xml"
db = Database(path)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    this is a view function which responds to requests for the top-level
    URL. It serves as the "controller" in MVC as it accesses both the model and the view.
    """

    # the button click within the view kicks off a POST request ...
    if request.method == "POST":

        acct_id = request.form["acctid"]
        acct_balance = db.balance(acct_id.upper())
        app.logger.debug(f"balance for {acct_id}: {acct_balance}")

    else:
        acct_balance = "N/A"

    return render_template("index.html", acct_balance = acct_balance)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
