# 🔗 URL Shortener https://url-shortener-blush-six.vercel.app/

A fast and lightweight full-stack URL shortener built with **FastAPI**, **SQLite**, and **React**. It converts long URLs into unique 6-character short links and tracks redirect statistics in real time.

---

## ✨ Features

- ✂️ **Shorten URLs** — Generate unique, collision-resistant 6-character short codes.
- 🔀 **Fast Redirects** — Redirect users instantly using HTTP 307 responses.
- 📊 **Click Analytics** — Track the number of visits for every shortened URL.

---

## 🛠️ Tech Stack

### Backend

- Python 3.12+
- FastAPI
- SQLAlchemy
- Pydantic v2

### Frontend

- React
- CSS3

### Database

- SQLite

### DevOps

- Docker
- Multi-stage Docker Build

---

## 🚀 Getting Started

### 🐳 Run with Docker (Recommended)

Build the Docker image:

```bash
docker build -f server/Dockerfile -t url-shortener .
```

Run the container:

```bash
docker run -d \
  -p 8000:8000 \
  -v $(pwd)/server/shortener.db:/app/server/shortener.db \
  --name url-shortener-app \
  url-shortener
```

Stop the container:

```bash
docker stop url-shortener-app
```

Remove the container:

```bash
docker rm url-shortener-app
```

Once the container is running:

| Service | URL |
|---------|-----|
| 🌐 Application | http://localhost:8000 |
| 📚 Swagger UI | http://localhost:8000/docs |
| 📄 ReDoc | http://localhost:8000/redoc |

---

### 💻 Local Development

Navigate to the backend:

```bash
cd server
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the development server:

```bash
python app/main.py
```

---

## 📌 Roadmap

- [X] URL shortening endpoint
- [X] Redirect endpoint
- [X] Click analytics
- [X] React dashboard
- [X] Search and filter links
- [X] Copy-to-clipboard button

---

## 📄 License

This project is licensed under the **MIT License**.