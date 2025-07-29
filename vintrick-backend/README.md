# File: README.md

## VinTrick Node.js + PostgreSQL Boilerplate

### Setup

1. **Clone the repo**
2. **Create `.env` from example**
3. **Start services**
   ```sh
   docker-compose up --build

----Backend----
docker-compose build
docker-compose up

docker-compose down
docker-compose build --no-cache
docker-compose up

npm install prisma@latest @prisma/client@latest


docker-compose down --remove-orphans -v
docker-compose build
docker-compose up -d
docker-compose run backend npx prisma migrate dev --name init


docker-compose up           # to run backend + db
# or, in dev: npx nodemon src/app.js (if not running in docker)


----Frontend----
cd vintrick-frontend
npm start

# use this to enter the container, must be in the right dir - $ cd Vintrick/vintrick-backend
docker-compose exec backend sh
# then 
 npx prisma migrate dev --name add-user-auth

# prisma studio to check on users table
http://localhost:5556/

docker-compose exec backend npx prisma studio --port 5556


git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Glip/Vintrick.git
git branch -M main
git push -u origin main



# Vintrick

A full-stack application for vineyard management and harvest tracking.

## 🔧 Tech Stack

* **Frontend:** React, Context API, custom CSS
* **Backend:** Python (FastAPI or Flask), Node.js (Express)
* **Database:** Prisma (likely PostgreSQL)
* **Other:** Docker, Excel upload tools

---

## 📁 Project Structure

```
Vintrick/
├── vintrick-frontend/      # React frontend
└── vintrick-backend/       # Python + Node.js backend with Prisma and APIs
```

---

## 🚀 Getting Started

### Prerequisites

* Node.js (v18+)
* Python (v3.10+)
* Docker (optional)

### Clone Repo

```bash
git clone https://github.com/GlipGlops-glitch/Vintrick.git
cd Vintrick
```

### Frontend Setup

```bash
cd vintrick-frontend
npm install
npm start
```

### Backend Setup

```bash
cd vintrick-backend
pip install -r requirements.txt  # or npm install if Node
python main.py                   # or node src/app.js
```

> Add `.env` file based on `.env.example` before running.

---

## 📌 Features

* 📊 Harvest Load Entry + Management
* 🔐 User Authentication
* 📈 Blend/Details/Reports Screens
* 🧾 Excel Upload Tool

---

## 📦 Scripts

You can create a combined dev script like:

```bash
# dev-start.sh
(cd vintrick-backend && npm start) &
(cd vintrick-frontend && npm start)
```

---

## 🧪 Testing

* Backend: `pytest` or `Jest`
* Frontend: `npm test` (Jest + React Testing Library)

---

## ✅ To-Do

* [ ] Add unit tests for all endpoints/components
* [ ] Setup CI via GitHub Actions
* [ ] Add linting + format checks
* [ ] Improve error handling in backend routes

---

## 📄 License

MIT



Read the repo: https://github.com/GlipGlops-glitch/Vintrick



git add .
git commit -m 
git push


cd Vintrick/vintrick-frontend/src
frontend_theme_zip.bat


### 📁 vintrick-backend/

- [.dockerignore](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/.dockerignore)
- [.env](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/.env)
- [Dockerfile](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/Dockerfile)
- [README.md](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/README.md)
- [dao.py](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/dao.py)
- [docker-compose.yml](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/docker-compose.yml)
- [index.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/index.js)
- [main.py](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/main.py)
- [models.py](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/models.py)
- [package.json](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/package.json)

#### 📁 prisma/
- [schema.prisma](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/prisma/schema.prisma)
- [migrations/](https://github.com/GlipGlops-glitch/Vintrick/tree/main/vintrick-backend/prisma/migrations)
  - Migration SQLs and `migration_lock.toml`

#### 📁 src/
- [app.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/app.js)
- [db.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/db.js)

#### 📁 src/routes/
- [auth.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/routes/auth.js)
- [harvestloads.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/routes/harvestloads.js)

#### 📁 src/controllers/
- [harvestloads.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/controllers/harvestloads.js)

#### 📁 Tools/
- [upload_harvest_loads.py](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/Tools/upload_harvest_loads.py)
- [harvest Loads.xlsx](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/Tools/harvest%20Loads.xlsx)


### 📁 vintrick-frontend/

- [.env](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/.env)
- [.gitignore](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/.gitignore)
- [.gitkeep](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/.gitkeep)
- [README.md](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/README.md)
- [fix.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/fix.js)
- [package-lock.json](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/package-lock.json)
- [package.json](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/package.json)

#### 📁 public/
- [favicon.ico](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/public/favicon.ico)
- [index.html](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/public/index.html)
- [logo192.png](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/public/logo192.png)
- [logo512.png](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/public/logo512.png)
- [manifest.json](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/public/manifest.json)
- [robots.txt](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/public/robots.txt)

#### 📁 src/
- [App.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/App.css)
- [App.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/App.js)
- [App.test.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/App.test.js)
- [index.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/index.css)
- [index.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/index.js)
- [logo.svg](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/logo.svg)
- [reportWebVitals.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/reportWebVitals.js)
- [setupTests.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/setupTests.js)

#### 📁 src/assets/
- [TEST.csv](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/assets/TEST.csv)
- [background.png](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/assets/background.png)
- [desktop.ini](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/assets/desktop.ini)
- [gif_Run.py](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/assets/gif_Run.py)
- [grape.png](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/assets/grape.png)
- [grape_loading.gif](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/assets/grape_loading.gif)
- [vintrick-logo.png](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/assets/vintrick-logo.png)

#### 📁 src/components/
- [AddEditHarvestLoadForm.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/AddEditHarvestLoadForm.js)
- [HarvestLoadFormBody.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/HarvestLoadFormBody.js)
- [HeaderBar.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/HeaderBar.css)
- [HeaderBar.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/HeaderBar.js)
- [NavBar.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/NavBar.js)
- [ProtectedRoute.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/ProtectedRoute.js)

#### 📁 src/context/
- [AuthContext.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/context/AuthContext.js)
- [SettingsContext.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/context/SettingsContext.js)

#### 📁 src/screens/
- [API_Screen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/API_Screen.css)
- [API_Screen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/API_Screen.js)
- [BlendDetailScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/BlendDetailScreen.css)
- [BlendDetailScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/BlendDetailScreen.js)
- [BlendsScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/BlendsScreen.css)
- [BlendsScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/BlendsScreen.js)
- [CalculatorsScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/CalculatorsScreen.css)
- [CalculatorsScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/CalculatorsScreen.js)
- [DataScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/DataScreen.css)
- [DataScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/DataScreen.js)
- [DetailsScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/DetailsScreen.css)
- [DetailsScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/DetailsScreen.js)
- [DocumentsScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/DocumentsScreen.css)
- [DocumentsScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/DocumentsScreen.js)
- [HarvestLoadFormSettings.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HarvestLoadFormSettings.js)
- [HarvestLoadsScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HarvestLoadsScreen.css)
- [HarvestLoadsScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HarvestLoadsScreen.js)
- [HomeScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HomeScreen.css)
- [HomeScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HomeScreen.js)
- [LoginScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/LoginScreen.js)
- [SettingsScreen.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/SettingsScreen.css)
- [SettingsScreen.js](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/SettingsScreen.js)
- [theme.css](https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/theme.css)



/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/README.md
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/.gitignore
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/.env
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/package.json
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/package-lock.json

/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/index.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/index.css
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/App.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/App.css
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/App.test.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/setupTests.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/reportWebVitals.js

/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/HeaderBar.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/HeaderBar.css
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/NavBar.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/NavBar.module.css
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/ProtectedRoute.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/AddEditHarvestLoadForm.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/components/HarvestLoadFormBody.js

/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/context/AuthContext.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/context/SettingsContext.js

/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HomeScreen.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HomeScreen.css
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HarvestLoadsScreen.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/HarvestLoadsScreen.css
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/SettingsScreen.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-frontend/src/screens/SettingsScreen.css



/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/README.md
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/Dockerfile
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/docker-compose.yml
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/.dockerignore
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/.env
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/models.py
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/dao.py
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/main.py
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/package.json

/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/app.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/db.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/routes/auth.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/routes/harvestloads.js
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/src/controllers/harvestloads.js

/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/prisma/schema.prisma
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/prisma/migrations/20250725180429_init/migration.sql
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/prisma/migrations/20250726000657_init/migration.sql
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/prisma/migrations/20250726223537_add_user_auth/migration.sql
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/prisma/migrations/migration_lock.toml

/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/Tools/upload_harvest_loads.py
/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/Tools/harvest%20Loads.xlsx

/read https://github.com/GlipGlops-glitch/Vintrick/blob/main/vintrick-backend/app/main.py
app/main.py

docker-compose build --no-cache
docker-compose up


Run stuff in the container 
docker-compose exec api python test.py


git status
git add .
git commit -m "CH"
git push

psql -U postgres -d db



# Commands Explanation

# docker-compose down:
Stops and removes all containers, networks, and volumes defined in the docker-compose.yml file.
This ensures a clean slate before rebuilding.

# docker-compose build --no-cache:
Rebuilds the images for the services defined in the docker-compose.yml file.
The --no-cache flag ensures that Docker does not use any cached layers, forcing a fresh build.

# docker-compose up:
Starts the containers defined in the docker-compose.yml file.
If the images are not already built, it will build them (but since you already ran docker-compose build, this step will just start the containers).

Optional Enhancements
If you want to run the containers in detached mode (in the background), use:

If you want to remove orphaned containers and volumes (e.g., from previous builds), you can use:

Full Rebuild Workflow
Here’s the complete workflow for rebuilding and starting the containers:

Testing After Rebuild
Check Logs:

Use docker-compose logs -f to monitor the logs and ensure everything starts correctly.
Access the Containers:

Use docker-compose exec <service-name> sh to enter a container (e.g., backend or api).
Verify Services:

Test the backend and frontend endpoints to ensure they are running as expected.