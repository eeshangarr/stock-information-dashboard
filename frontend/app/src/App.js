import React, {useState} from 'react' // Import React and useState
import "./App.css" // Import .css file for styling the frontend 
import axios from 'axios' // Axios is used to communicate with the backend

export default function App() {
  // Define frontend variables
  const [tickerSymbol, setTickerSymbol] = useState('')
  const [currentPrice, setCurrentPrice] = useState('')
  const [totalRevenue, setTotalRevenue] = useState('')
  const [shortName, setShortName] = useState('')
  const [address, setAddress] = useState('')
  const [website, setWebsite] = useState('')
  const [keyFigure, setKeyFigure] = useState('')
  const [grossProfits, setGrossProfits] = useState('')
  const [grossMargins, setGrossMargins] = useState('')
  const [earningsGrowth, setEarningsGrowth] = useState('')
  const [companyRating, setCompanyRating] = useState('')
  const [newsLinks, setNewsLinks] = useState([])
  const [googleMapsLink, setGoogleMapsLink] = useState('')

  // Backend and frontend communication
  const submit = async (event) => {
    event.preventDefault();
    // Send ticker symbol to backend
    await axios.post("http://localhost:5000/stockInformation", {tickerSymbol})
      // Get stock information from the backend
      .then(response => {const {data} = response; setTotalRevenue(data.totalRevenue); setCurrentPrice(data.currentPrice); setShortName(data.shortName); setAddress(data.address); setWebsite(data.website); setKeyFigure(data.keyFigure); setGrossProfits(data.grossProfits); setGrossMargins(data.grossMargins); setEarningsGrowth(data.earningsGrowth); setCompanyRating(data.companyRating); setNewsLinks(data.newsLinks); setGoogleMapsLink(data.googleMapsLink)})
  };

  // Frontend for user input and information display
  return (
    <div className = "frontend">
    <div className = "title">TickerInsight</div>
    <form onSubmit = {submit}>
    <div className = "input"><input placeholder='Enter Ticker Symbol' class = "tickerSymbol" type = "text" value = {tickerSymbol} onChange = {(event) => setTickerSymbol(event.target.value)}/></div>
    <div className = "button"><button className = "submitButton" type = "submit">Submit</button></div>
    </form>
      <div className = "leftSide">
      <div className = "businessTop">
      Total Revenue: {totalRevenue}
      <p></p>
      Current Price: {currentPrice}
      <p></p>
      Short Name: {shortName}
      </div>
      <div className = "googleMaps">Address: <a href = {googleMapsLink}>{address}</a></div>
      <div className = "companyWebsite">Website: <a href = {website}>{website}</a></div>
      <div className = "businessBottom">
      <p></p>
      Key Figure: {keyFigure}
      <p></p>
      Gross Profits: {grossProfits}
      <p></p>
      Gross Margins: {grossMargins}
      <p></p>
      Earnings Growth: {earningsGrowth}
      </div>
      <p></p>
      </div>
      <div className = "sentimentAnalysis">
      <u>Sentiment Analysis</u> 
      <div className= "rating">{companyRating}</div>
      </div>
      <p></p>
      <div className = "news">
      <u className = "links">News Links</u>
      <p></p>
      <ul className="map">
        {newsLinks.map(function (link, index) {
          return (
            <div key={index}>
              <a href={link}>Link {index + 1}</a>
              <br/> 
            </div>
          );
        })}
      </ul>
      </div>
    </div>
  );
}
