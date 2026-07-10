# 🌿 Plant Disease Detection

A full-stack AI web application that identifies plant leaf diseases from a
photo, using a PyTorch model served through a FastAPI backend and a
React + Tailwind + shadcn/ui frontend.

> Status: 🚧 scaffolding stage — features are being implemented incrementally.
> See the roadmap below for what's done vs. planned.

## Features

- [ ] Secure signup/login (JWT + bcrypt)
- [ ] Upload a leaf image and get a disease prediction + confidence score
- [ ] Top-3 predictions with disease info, causes, symptoms, treatment, prevention
- [ ] Prediction history with search, filter, delete, pagination
- [ ] User profile (edit info, change password)
- [ ] Responsive, dark-mode-supported dashboard UI

## Tech Stack

| Layer      | Choice                                            |
|------------|----------------------------------------------------|
| Frontend   | React (Vite), Tailwind CSS, shadcn/ui, React Router, Axios |
| Backend    | FastAPI, PyTorch, Uvicorn                          |
| Auth       | JWT, bcrypt (via passlib)                          |
| Database   | PostgreSQL + SQLAlchemy + Alembic                  |
| Deployment | Frontend → Vercel, Backend → Render                |

## Folder Structure

```
plant-disease-app/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app, CORS, lifespan/model loading
│   │   ├── routes/          # HTTP endpoints (auth, predict, history, profile)
│   │   ├── services/        # Business logic (model_service, auth_service, ...)
│   │   ├── models/          # SQLAlchemy ORM models + Pydantic schemas
│   │   ├── auth/            # JWT creation/verification, password hashing
│   │   ├── utils/           # Config/settings, helpers
│   │   └── database/        # DB session/engine setup
│   ├── model/
│   │   ├── model.pth        # <-- put your trained weights here (gitignored)
│   │   └── predict.py       # Model loading + inference logic
│   ├── requirements.txt
│   ├── render.yaml
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/      # Reusable UI (Navbar, Footer, Card, etc.)
│   │   ├── pages/           # Home, Login, Signup, Dashboard, Prediction, History, Profile, 404
│   │   ├── hooks/           # Custom hooks (useAuth, usePredict, ...)
│   │   ├── context/         # Auth context/provider
│   │   ├── lib/             # Axios instance, utils
│   │   └── assets/
│   ├── package.json
│   └── .env.example
└── README.md
```

## Installation

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # then fill in real values
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

## API Documentation

_Filled in as each endpoint is implemented. FastAPI also auto-generates
interactive docs at `/docs` once the server is running._

| Method | Endpoint         | Auth required | Description                        |
|--------|------------------|----------------|-------------------------------------|
| POST   | /signup          | No             | Create a new account                |
| POST   | /login           | No             | Authenticate, returns JWT           |
| POST   | /predict         | Yes            | Upload an image, get prediction     |
| GET    | /history         | Yes            | List past predictions               |
| DELETE | /history/{id}    | Yes            | Delete a prediction record          |
| GET    | /profile         | Yes            | Get current user's profile          |

## Deployment

- **Frontend (Vercel):** connect the GitHub repo, set root directory to
  `frontend/`, add `VITE_API_BASE_URL` pointing at the Render backend URL.
- **Backend (Render):** connect the repo, root directory `backend/`,
  Render will pick up `render.yaml`. Set `JWT_SECRET_KEY` and
  `DATABASE_URL` (from a Render PostgreSQL instance) in the dashboard.

## Screenshots

_Add screenshots here once the UI is built:_
- Home page: `![Home](docs/screenshots/home.png)`
- Dashboard: `![Dashboard](docs/screenshots/dashboard.png)`
- Prediction result: `![Prediction](docs/screenshots/prediction.png)`

## Future Improvements

- Rate limiting on `/predict` (slowapi is already in requirements.txt)
- Email verification on signup
- Model explainability (Grad-CAM overlay on uploaded image)
- Admin dashboard for monitoring usage

## Roadmap / Build Log

1. ✅ Project scaffolding (this step)
2. ⬜ Database models + PostgreSQL connection
3. ⬜ Auth (signup/login, JWT, bcrypt)
4. ⬜ Model integration (`predict.py`, `/predict` endpoint)
5. ⬜ History + profile endpoints
6. ⬜ Frontend auth pages + routing
7. ⬜ Frontend dashboard + prediction UI
8. ⬜ Frontend history/profile pages + polish (dark mode, toasts, skeletons)
9. ⬜ Deployment (Render + Vercel)
