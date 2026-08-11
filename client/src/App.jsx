import { useEffect, useState } from "react";
import "./App.css";

const API = process.env.REACT_APP_API_URL || "http://localhost:8000/api";
const BASE_URL = API.replace(/\/api\/?$/, "");

function App() {
  const [url, setUrl] = useState("");
  const [links, setLinks] = useState(() => {
    try {
      const saved = localStorage.getItem("lastlink");
      return saved ? JSON.parse(saved) : null;
    } catch (e) {
      return null;
    }
  });

  useEffect(() => {
    if (!links?.short_code) return;

    fetch(`${API}/links/${links.short_code}`)
      .then((res) => {
        if (!res.ok) throw new Error("Ссылка не найдена");
        return res.json();
      })
      .then((updatedLink) => {
        setLinks(updatedLink);
        localStorage.setItem("lastlink", JSON.stringify(updatedLink));
      })
      .catch((err) => {
        localStorage.removeItem("lastlink");
        setLinks(null);
      });
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    fetch(`${API}/shorten`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ original_url: url }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Link Error");
        }
        return res.json();
      })
      .then((newLink) => {
        setUrl("");
        setLinks(newLink);
        localStorage.setItem("lastlink", JSON.stringify(newLink));
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
