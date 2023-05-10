from flask import Flask, request, jsonify
from flask_cors import cross_origin
import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/tickerSymbol", methods = ["POST", "OPTIONS"])
@cross_origin()
def tickerSymbol():
    # Get ticker symbol from frontend
    if request.method == "POST":
        tickerSymbol = str(request.json.get("tickerSymbol"))
        tickerInformation = yf.Ticker(tickerSymbol).info
        # Get certain information about the stock
        shortName = str(tickerInformation["shortName"]) 
        currentPrice = str(tickerInformation["currentPrice"]) 
        totalRevenue = str(tickerInformation["totalRevenue"])
        address = str(tickerInformation["address1"]) +  ", " + str(tickerInformation["city"]) +  ", " + str(tickerInformation["state"]) +  ", " + str(tickerInformation["zip"]) 
        website = str(tickerInformation["website"])
        keyFigure = str(tickerInformation["companyOfficers"][0]["name"])        
        totalRevenue = str(tickerInformation["totalRevenue"])
        grossProfits = str(tickerInformation["grossProfits"])
        grossMargins = str(tickerInformation["grossMargins"])
        earningsGrowth = str(tickerInformation["earningsGrowth"])
    return {"currentPrice" : currentPrice, "totalRevenue" : totalRevenue, "shortName" : shortName, "address" : address, "website" : website, "keyFigure" : keyFigure, "totalRevenue" : totalRevenue, "grossProfits" : grossProfits, "grossMargins" : grossMargins, "earningsGrowth" : earningsGrowth}, 200