import { useState, useEffect } from "react";

function App() {
  const [card, setCard] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5001/api/card/4")
      .then((res) => {
        if (!res.ok) throw new Error("No card found");
        return res.json();
      })
      .then((data) => setCard(data))
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p>Error: {error}</p>;
  if (!card) return <p>Loading...</p>;

  return (
    <div>
      <h1>{card.front}</h1>
      <h1>{card.back}</h1>
    </div>
  );
}

export default App;