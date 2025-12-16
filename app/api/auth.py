from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google.cloud import firestore
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

db = firestore.Client()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class LoginRequest(BaseModel):
    email: str
    password: str


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/admin/auth/login")
def login(req: LoginRequest):
    docs = db.collection("admins").where("email", "==", req.email).stream()
    user = next(docs, None)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user_data = user.to_dict()

    if not pwd_context.verify(req.password, user_data["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": req.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
