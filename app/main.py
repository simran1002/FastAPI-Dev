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

    async with engine.begin() as conn:
        
        await conn.run_sync(Base.metadata.create_all)
    
    yield
    
    await engine.dispose()

app = FastAPI(
    title="KPA Form Data API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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