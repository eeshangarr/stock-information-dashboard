from flask import Flask, request, jsonify
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
        print(tickerInformation)
        # Get certain information about the stock
        shortName = str(tickerInformation["shortName"]) 
        currentPrice = str(tickerInformation["currentPrice"]) 
        totalRevenue = str(tickerInformation["totalRevenue"])
        address = str(tickerInformation["address1"]) +  ", " + str(tickerInformation["city"]) +  ", " + str(tickerInformation["state"]) +  ", " + str(tickerInformation["zip"]) 
        website = str(tickerInformation["website"])
        keyFigure = str(tickerInformation["companyOfficers"][0]["name"])        
        totalRevenue = str(tickerInformation["totalRevenue"])
    return {"currentPrice" : currentPrice, "totalRevenue" : totalRevenue, "shortName" : shortName, "address" : address, "website" : website, "keyFigure" : keyFigure, "totalRevenue" : totalRevenue}, 200