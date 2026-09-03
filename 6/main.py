from fastapi import FastAPI
import uvicorn
from web.route.user_controller import user_router

app = FastAPI(
    title="Users API",
    version="1.0"
)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)