from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.firebase_init import db
from app.core.security import verify_password

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(req: LoginRequest):
    admin_ref = db.collection("admins").document(req.email).get()
    if not admin_ref.exists:
        raise HTTPException(status_code=401, detail="Email not found")

    admin_data = admin_ref.to_dict()
    if not verify_password(req.password, admin_data["password"]):
        raise HTTPException(status_code=401, detail="Wrong password")

    return {"message": "Login successful!"}
