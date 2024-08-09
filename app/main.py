from fastapi import FastAPI
from .routes import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)
