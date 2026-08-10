import { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [links, setLinks] = useState(null);

  const API = process.env.REACT_APP_API_URL || "http://localhost:8000/api";
  const BASE_URL = API.replace(/\/api\/?$/, "");

  function handleSubmit(e) {
    e.preventDefault();
    fetch(`${API}/shorten`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ original_url: url }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Ошибка создания ссылки");
        }
        return res.json();
      })
      .then((newLink) => {
        setUrl("");
        setLinks(newLink);
      });
  }

  return (
    <div className="App">
      <h1>URL SHORTENER</h1>

      <form className="shortener-form" onSubmit={handleSubmit}>
        <input
          type="text"
          className="url-input"
          placeholder="Enter here link"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button className="submit-btn" type="submit">
          to shorten
        </button>
      </form>

      {links && (
        <div className="links-list">
          <div className="linksItem">
            <h1>{links.original_url}</h1>
            <div className="short-url-div">
              <a
                href={`${BASE_URL}/${links.short_code}`}
                target="_blank"
                rel="noreferrer"
                className="short-url"
              >
                {`${BASE_URL}/${links.short_code}`}
              </a>
              <h2 className="clicks-badge">link clicks: {links.clicks}</h2>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
