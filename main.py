from fastapi import FastAPI, Request, status
# from .models import Base
# from .database import engine
# from .routers import art, home, paintings
from routers import home,art,paintings
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

# Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(home.router)
app.include_router(art.router)
app.include_router(paintings.router)