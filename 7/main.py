from fastapi import FastAPI
import uvicorn
from web.route.auth_controller import auth_router

app = FastAPI(
    title="JWT Auth API",
    version="1.0"
)

app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)