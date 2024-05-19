from fastapi import FastAPI
from route.user import user_router

app = FastAPI()
app.include_router(user_router)