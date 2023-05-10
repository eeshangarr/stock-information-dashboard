import React, {useState} from 'react' 
import axios from 'axios' // Axios is used to communicate with the backend

export default function App() {
  const [tickerSymbol, setTickerSymbol] = useState('')
  const [currentPrice, setCurrentPrice] = useState('')
  const [totalRevenue, setTotalRevenue] = useState('')
  const [shortName, setShortName] = useState('')
  const [address, setAddress] = useState('')
  const [website, setWebsite] = useState('')
  const [keyFigure, setKeyFigure] = useState('')

  // Send ticker symbol to backend
  const submit = async (event) => {
    event.preventDefault();
    await axios.post("http://localhost:5000/tickerSymbol", {tickerSymbol})
      .then(response => {const {data} = response; setTotalRevenue(data.totalRevenue); setCurrentPrice(data.currentPrice); setShortName(data.shortName); setAddress(data.address); setWebsite(data.website); setKeyFigure(data.keyFigure)})
  };

  // Initial frontend for user input
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

    </div>
    </div>
  );
}
