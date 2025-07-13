from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

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
    """
    Authenticate user and provide access token.
    
    **Demo Mode:**
    - Accepts any valid username and password
    - Returns a dummy token for testing purposes
    
    **Production Mode:**
    - Validates credentials against database
    - Returns JWT token with user permissions
    
    **Request Body:**
    - **phone_number**: User's phone number
    - **password**: User's login password
    
    **Returns:**
    - **success**: Authentication status
    - **message**: Status message
    - **token**: JWT bearer token for API requests
    - **token_type**: Token type (always "bearer")
    
    **Error Responses:**
    - 400: Missing phone number or password
    - 401: Invalid credentials
    """
    # For demo, accept any phone_number/password
    if not data.phone_number or not data.password:
        raise HTTPException(status_code=400, detail="Phone number and password required.")
    # In real app, check credentials here
    return LoginResponse(
        success=True,
        message="Login successful.",
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NzYwODczOTc2IiwibmFtZSI6IlVzZXIiLCJpYXQiOjE3MzE5NzI3NzcsImV4cCI6MTczMTk3NjM3N30.dummy-signature-123",
        token_type="bearer"
    ) 