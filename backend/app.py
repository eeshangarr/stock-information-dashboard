from flask import Flask, request, jsonify
from flask_cors import cross_origin
import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from statistics import mean

def getGoogleMapsLink(address):
    # Define a place to store the new Google Maps address
    newAddress = " " 

    # Iterate through address and add in a "+" where there is a space
    for character in address:
        if character == ' ':
            newAddress += "+"
        elif character != ' ':
            newAddress += character

    # Append to the original Google Maps link
    googleMapsLink = "https://www.google.com/maps/place/" + newAddress

    return googleMapsLink

def convertToDollar(number):
    # Define a new string to return the dollar amount in
    dollarAmount = ""

    # Define blocks of numbers
    blocks = []

    # Get every 3 numbers until there are no more numbers
    index = len(number) - 1
    while index >= 0:
        block = number[max(0, index - 2):index + 1]
        blocks.append(block)
        index -= 3

    # Iterate backwards through each unit
    for unit in reversed(blocks):
        dollarAmount += unit
        dollarAmount += ","
    
    # Add "$", get rid of extra comma at the end, and add a cents amount
    dollarAmount = "$" + dollarAmount
    dollarAmount = dollarAmount[: -1]
    dollarAmount += ".00"

    # Return the dollar amount version of the number string
    return dollarAmount

def companyNews(company):
    # Define news titles and links list
    newsTitles = []
    newsLinks = []

    # Make a request to the News API, which returns a JSON dictionary with news articles
    response = requests.get("https://newsapi.org/v2/everything?q=" + company + "&apiKey=feb512529033419d92ef36b32155b369")


    # Get news article titles and links
    index = 0
    while index < 10:
        # Keep number of news links under 3
        if len(newsLinks) < 3:
            newsLinks.append(response.json()["articles"][index]["url"])
        newsTitles.append(response.json()["articles"][index]["title"] + " ")
        index += 1

    # Return news titles
    return [newsTitles, newsLinks]

def sentimentAnalysis(titles):
    # Define a list of scores
    scores = []

    # Define SentimentIntensityAnalyzer object
    sentiment = SentimentIntensityAnalyzer()

    # Go through titles
    for title in titles:
        # Find polarity score for each title and store in scores
        scores.append(sentiment.polarity_scores(title))

    # Define a place to score each of the scores
    negativeScores = []
    neutralScores = []
    positiveScores = []

    # Store the scores
    for dictionary in scores:
        for key, value in dictionary.items():
            if key == 'neg':
                negativeScores.append(value)
            if key == 'neu':
                neutralScores.append(value)
            if key == 'pos':
                positiveScores.append(value)

    # Find the overall average of each type of score and store in a dictionary
    averageScores = {"Negative" : mean(negativeScores), "Positive" : mean(positiveScores), "Neutral" : mean(neutralScores)}

    # Find the rating with the highest average score
    maximumScore = averageScores["Negative"]
    rating = ""
    for key, value in averageScores.items():
        if value > maximumScore:
            maximumScore = value
            rating = key

    # Return the rating
    return rating


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
        currentPrice = "$" + currentPrice
        totalRevenue = convertToDollar(str(tickerInformation["totalRevenue"]))
        address = str(tickerInformation["address1"]) +  ", " + str(tickerInformation["city"]) +  ", " + str(tickerInformation["state"]) +  ", " + str(tickerInformation["zip"]) 
        googleMapsLink  = getGoogleMapsLink(address)
        website = str(tickerInformation["website"])
        keyFigure = str(tickerInformation["companyOfficers"][0]["name"])        
        grossProfits = convertToDollar(str(tickerInformation["grossProfits"]))
        grossMargins = str(tickerInformation["grossMargins"])
        earningsGrowth = str(tickerInformation["earningsGrowth"])

        # Get company name to get current company news
        companyName = ""
        for character in shortName:
            if character == ' ':
                break
            else:
                companyName += character

        # Get company rating based on sentiment analysis function
        companyRating = sentimentAnalysis(companyNews(companyName)[0])

        print("googleMapsLink: " + googleMapsLink)
        # Return dictionary with stock infomration
        return {"currentPrice" : currentPrice, "totalRevenue" : totalRevenue, "shortName" : shortName, "address" : address, "website" : website, "keyFigure" : keyFigure, "totalRevenue" : totalRevenue, "grossProfits" : grossProfits, "grossMargins" : grossMargins, "earningsGrowth" : earningsGrowth, "companyRating" : companyRating, "newsLinks" : companyNews(companyName)[1], "googleMapsLink" : googleMapsLink}, 200
    
    return "404", 404