from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/tickerSymbol", methods = ["POST", "OPTIONS"])
@cross_origin()
def tickerSymbol():
    # Get ticker symbol from frontend
    if request.method == "POST":
        print("Ticker Symbol: " + str(request.json.get("tickerSymbol")))
    return "200", 200