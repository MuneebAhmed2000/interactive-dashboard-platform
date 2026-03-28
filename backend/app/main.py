from fastapi import FastAPI, WebSocket, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json
import random
import asyncio

from .database import SessionLocal, engine
from .models import DashboardLayout, User, Base
from .auth import hash_password, verify_password, create_access_token, decode_token

Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📊 Fake data
def generate_fake_data():
    return {
        "company": "Demo Corp",
        "revenue": random.randint(1000, 10000),
        "users": random.randint(100, 5000)
    }

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔐 Get current user from token
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload["sub"]

# -----------------------------
# 🔐 AUTH ROUTES
# -----------------------------

@app.post("/register")
def register(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == form.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="User exists")

    user = User(
        username=form.username,
        password=hash_password(form.password)
    )

    db.add(user)
    db.commit()
    return {"status": "registered"}

@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()

    if not user or not verify_password(form.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# -----------------------------
# 📊 DATA
# -----------------------------

@app.get("/data")
def get_data():
    return generate_fake_data()

# 💾 SAVE layout
@app.post("/layout")
def save_layout(layout: dict, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    existing = db.query(DashboardLayout).filter(DashboardLayout.user_id == user).first()

    if existing:
        existing.layout = layout
    else:
        db.add(DashboardLayout(user_id=user, layout=layout))

    db.commit()
    return {"status": "saved"}

# 📥 LOAD layout
@app.get("/layout")
def get_layout(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    layout = db.query(DashboardLayout).filter(DashboardLayout.user_id == user).first()
    return layout.layout if layout else {}

# -----------------------------
# ⚡ WEBSOCKET
# -----------------------------

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_text(json.dumps(generate_fake_data()))
        await asyncio.sleep(2)