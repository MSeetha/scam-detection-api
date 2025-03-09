import React, { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const checkScam = async () => {
    const response = await axios.post("http://127.0.0.1:8000/predict/", { text });
    setResult(response.data.prediction);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Social Media Scam Detection</h2>
      <textarea 
        rows="4" cols="50" 
        placeholder="Enter a message to check for scam..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <button onClick={checkScam}>Check Scam</button>
      {result && <h3>Prediction: {result}</h3>}
    </div>
  );
}

export default App;
