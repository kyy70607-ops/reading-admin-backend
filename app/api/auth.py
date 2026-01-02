from fastapi import APIRouter, Header, HTTPException
from app.core.firebase_admin import verify_token

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/me")
def admin_me(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token")

    try:
        token = authorization.replace("Bearer ", "")
        user = verify_token(token)
        return {
            "uid": user["uid"],
            "email": user.get("email")
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

