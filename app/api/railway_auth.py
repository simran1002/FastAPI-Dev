from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import secrets
import base64
import json
from ..config import settings

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    phone_number: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    message: str
    token: str
    token_type: str = "bearer"

@router.post("/login", 
    response_model=LoginResponse,
    summary="User Login",
    description="Authenticate user and return access token for API access",
    response_description="Login successful with access token"
)
def login(data: LoginRequest):

    if not data.phone_number or not data.password:
        raise HTTPException(status_code=400, detail="Phone number and password required.")
    
    payload = {
        "sub": data.phone_number,
        "name": "User",
        "iat": datetime.utcnow().isoformat(),
        "exp": (datetime.utcnow() + timedelta(hours=24)).isoformat(), 
        "jti": secrets.token_urlsafe(16)  
    }
    
    try:

        payload_str = json.dumps(payload)
        payload_bytes = payload_str.encode('utf-8')
        payload_b64 = base64.urlsafe_b64encode(payload_bytes).decode('utf-8')
        
    
        signature = secrets.token_urlsafe(32)
        

        token = f"{payload_b64}.{signature}"
        
        return LoginResponse(
            success=True,
            message="Login successful.",
            token=token,
            token_type="bearer"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Token generation failed") 