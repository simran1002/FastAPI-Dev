from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from .config import settings
from .database import engine, Base, AsyncSessionLocal
from .api import auth_router, forms_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    # Startup
    async with engine.begin() as conn:
        # Create tables if they don't exist
        await conn.run_sync(Base.metadata.create_all)
    
    yield
    
    # Shutdown
    await engine.dispose()


# Create FastAPI application
app = FastAPI(
    title="KPA Form Data API",
    description="""
    # KPA Form Data API
    
    A comprehensive FastAPI backend for managing Kisan Parivahan App (KPA) form data and Railway Forms.
    
    ## Features
    
    * **Authentication** - Secure login system with JWT tokens
    * **KPA Form Data** - Railway maintenance and inspection forms
    * **PostgreSQL Database** - Robust data storage with async operations

    
    ## Quick Start
    
    1. **Health Check**: `GET /health`
    2. **Authentication**: `POST /api/auth/login`
    3. **Submit Forms**: Use the respective endpoints below
    
    ## API Categories
    
    * **Health & Documentation** - System status and API docs
    * **Authentication** - User login and token management
    * **KPA Form Data** - Railway maintenance and inspection forms
    
    ## Database
    
    This API uses PostgreSQL with async SQLAlchemy for optimal performance.
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
    contact={
        "name": "KPA API Support",
        "email": "support@kpa-api.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "message": str(exc)}
    )


# Health check endpoint
@app.get("/health", 
    tags=["Health & Documentation"],
    summary="Health Check",
    description="Check if the API is running and healthy",
    response_description="API health status and version information"
)
async def health_check():
    """
    Health check endpoint to verify API status.
    
    Returns:
        - **status**: Current health status
        - **message**: Status message
        - **version**: API version
        - **database**: Database connection status
    """
    return {
        "status": "healthy",
        "message": "KPA Form Data API is running",
        "version": "1.0.0",
        "database": "PostgreSQL connected"
    }


# Root endpoint
@app.get("/", 
    tags=["Health & Documentation"],
    summary="API Information",
    description="Get basic API information and available endpoints"
)
async def root():
    """
    Root endpoint providing API information and navigation.
    
    Returns:
        - **message**: Welcome message
        - **version**: API version
        - **docs**: Link to Swagger documentation
        - **redoc**: Link to ReDoc documentation
        - **endpoints**: Available API categories
    """
    return {
        "message": "Welcome to KPA Form Data API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "health": "/health",
            "authentication": "/api/auth/login",
            "kpa_form_data": "/api/forms/"
        }
    }


# Include routers
app.include_router(auth_router)
app.include_router(forms_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    ) 