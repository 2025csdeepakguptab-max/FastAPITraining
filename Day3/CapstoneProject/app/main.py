from fastapi import FastAPI
from app.config import settings
from app.database import ping_database
from app.routers import users
from app.routers import categories
#creates faspapi app instance 
app =FastAPI(title = settings.APP_NAME)

# Include the users router
app.include_router(users.router)
app.include_router(categories.router)

#this function runs once when the server starts.It checks the dB connection
@app.on_event("startup")
def on_startup():
    if ping_database():
        print(f"[startup] Successfully connected to MongoDB. App Name: {settings.APP_NAME}")
    else:
        raise RuntimeError("Failed to connect to MongoDB. Please check your connection settings.")
    
@app.get("/",tags=["Health"])
def health_check():
    return {"status": "OK", "app": settings.APP_NAME}