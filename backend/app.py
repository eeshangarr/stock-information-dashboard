from flask import Flask, request
from flask_cors import cross_origin
import yfinance as yf

app = Flask(__name__)

@app.route("/tickerSymbol", methods = ["POST", "OPTIONS"])
@cross_origin()
def tickerSymbol():
    # Get ticker symbol from frontend
    if request.method == "POST":
        tickerSymbol = str(request.json.get("tickerSymbol"))
        tickerInformation = yf.Ticker(tickerSymbol).info
        # Get the current price of the stock
        currentPrice = tickerInformation["currentPrice"] 
        print("tickerInformation: " + str(tickerInformation))
    return "200", 200