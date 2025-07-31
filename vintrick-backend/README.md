# Vintrick Backend

Vintrick is a full-stack vineyard management and harvest tracking application built with a modern Python/FastAPI backend and a React frontend. It enables seamless tracking of harvest loads, user authentication, data analysis, and Excel data import/export, all containerized with Docker for easy development and deployment.

---

## 🚀 Overview

**Vintrick** powers the operations of vineyards by providing:
- Efficient harvest load entry, browsing, and editing
- User authentication
- Excel import tools for harvest data
- RESTful API for integration
- Easy local development and deployment with Docker Compose
- Extensible codebase (Python/FastAPI, SQL Server)
- Frontend: React (see [vintrick-frontend](../vintrick-frontend/README.md))

---

## 🗂️ Project Structure

```
Vintrick/
├── vintrick-frontend/      # React frontend (see its README for details)
└── vintrick-backend/       # Python FastAPI backend + SQL Server (this folder)
    ├── app/                # Main backend application code
    │   ├── crud/           # CRUD service modules
    │   ├── models/         # SQLAlchemy ORM models
    │   ├── schemas/        # Pydantic schemas for API
    │   ├── api/            # FastAPI routers
    │   ├── core/           # DB, config, etc.
    │   └── main.py         # FastAPI app entrypoint
    ├── Tools/              # Excel upload scripts and data
    ├── docker-compose.yml  # Multi-container orchestration
    ├── Dockerfile          # Backend image build
    ├── requirements.txt    # Python dependencies
    ├── .env.example        # Env variable template
    └── README.md           # (This file)










```

---

## 🛠️ Tech Stack

- **Backend:** Python 3.11, FastAPI, SQLAlchemy, Pydantic
- **Database:** Microsoft SQL Server 2022 (Dockerized with mssql)
- **Frontend:** React (see `vintrick-frontend`)
- **DevOps:** Docker, Docker Compose, dotenv
- **Utilities:** Pandas (Excel upload), requests

---

## ⚡ Quick Start Cheat Sheet

### 🐳 Docker Compose (recommended)

```sh
# Build and start all services (API & SQL Server)
docker-compose up --build

# Rebuild without cache (if you've changed requirements)
docker-compose build --no-cache
docker-compose up

# Stop and remove containers/networks/volumes
docker-compose down
# Or remove orphans and volumes
docker-compose down --remove-orphans -v

# Enter the API container shell
docker-compose exec api sh
```

### 🐍 Python (local development)

```sh
cd vintrick-backend
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
# Make sure SQL Server is running (see above)
python -m app.main
```

### 📝 Environment Variables

Copy `.env.example` to `.env` and fill in your settings for DB, etc.

---

## 📊 Features

- CRUD for Harvest Loads (`/api/harvestloads`)
- Pagination & infinite scroll support
- Excel batch uploader (`Tools/upload_harvest_loads.py`)
- User authentication (API)
- CORS enabled for frontend integration
- Modern error handling and logging

---

## 🧪 Testing

```sh
# Test DB connection
python tools/test_conn.py

# Test POSTing a harvest load
python tools/test_post_one.py
```

---

## 🛠️ Useful Scripts

```sh
# Upload all harvest loads from Excel file
python Tools/upload_harvest_loads.py

# Create DB tables (using SQL script)
python tools/SQL/scripts/create_harvestloads.py
```

---

## 🧩 API Reference

### Harvest Loads

- `GET /api/harvestloads?skip=0&limit=50`  
  List harvest loads (paginated, most recent first)

- `POST /api/harvestloads`  
  Add a new harvest load (JSON body)

- `GET /api/harvestloads/{uid}`  
  Retrieve a specific harvest load

- `PATCH /api/harvestloads/{uid}`  
  Update a harvest load

- `DELETE /api/harvestloads/{uid}`  
  Delete a harvest load

See the included Postman collection:  
[vintrick-backend/tools/Vintrick-API.postman_collection.json](tools/Vintrick-API.postman_collection.json)

---

## 🐞 Troubleshooting & Tips

- If you get serialization errors, make sure Pydantic schemas are used for API responses.
- SQL Server default admin password is set in `docker-compose.yml` (change in production!).
- Use `docker-compose logs -f` to monitor logs.
- For infinite scroll, use the `skip` and `limit` query parameters in your frontend.

---

## 🎨 Frontend

See [`vintrick-frontend/README.md`](../vintrick-frontend/README.md) for setup and usage.

---

## 📝 License

MIT

---

## ✨ Contributing

1. Fork this repo
2. Create your branch (`git checkout -b feature/foo`)
3. Commit your changes
4. Push to the branch (`git push origin feature/foo`)
5. Open a Pull Request

---

## 🔗 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Docker Compose](https://docs.docker.com/compose/)
- [React](https://reactjs.org/)


## Personal use
# Build and start all services (API & SQL Server)
docker-compose up --build

# Rebuild without cache (if you've changed requirements)
docker-compose build --no-cache
docker-compose up

# Stop and remove containers/networks/volumes
docker-compose down
# Or remove orphans and volumes
docker-compose down --remove-orphans -v