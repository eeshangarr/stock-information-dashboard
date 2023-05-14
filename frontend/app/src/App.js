import React, {useState} from 'react' 
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

  // Backend and frontend communication
  const submit = async (event) => {
    event.preventDefault();
    // Send ticker symbol to backend
    await axios.post("http://localhost:5000/tickerSymbol", {tickerSymbol})
      // Get stock information from the backend
      .then(response => {const {data} = response; setTotalRevenue(data.totalRevenue); setCurrentPrice(data.currentPrice); setShortName(data.shortName); setAddress(data.address); setWebsite(data.website); setKeyFigure(data.keyFigure); setGrossProfits(data.grossProfits); setGrossMargins(data.grossMargins); setEarningsGrowth(data.earningsGrowth); setCompanyRating(data.companyRating)})
  };

  // Initial frontend for user input and information display
  return (
    <div>
    <div>
    <form onSubmit = {submit}>
    <input placeholder='Enter Ticker Symbol' class = "tickerSymbol" type = "text" value = {tickerSymbol} onChange = {(event) => setTickerSymbol(event.target.value)}/>
    <button type = "submit">Submit</button>
    </form>
    </div>
    <div>
      Total Revenue: {totalRevenue}
      <p></p>
      Current Price: {currentPrice}
      <p></p>
      Short Name: {shortName}
      <p></p>
      Address: {address}
      <p></p>
      Website: {website}
      <p></p>
      Key Figure: {keyFigure}
      <p></p>
      Gross Profits: {grossProfits}
      <p></p>
      Gross Margins: {grossMargins}
      <p></p>
      Earnings Growth: {earningsGrowth}
      <p></p>
      Sentiment Analysis: {companyRating}
    </div>
    </div>
  );
}
