import React, {useState} from 'react' 
import axios from 'axios' // Axios is used to communicate with the backend


export default function App() {
  const [tickerSymbol, setTickerSymbol] = useState('')

  const submit = async (event) => {
    event.preventDefault();
    await axios.post("http://localhost:5000/tickerSymbol", {tickerSymbol});
  };

  return (
    <form onSubmit = {submit}>
    <input placeholder='Enter Ticker Symbol' class = "tickerSymbol" type = "text" value = {tickerSymbol} onChange = {(event) => setTickerSymbol(event.target.value)}/>
    <button type = "submit">Submit</button>
    </form>
  );
}
