from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .routers import users, tasks
from .database import Base, engine

app = FastAPI()

# create database tables
Base.metadata.create_all(bind=engine)

# templates
templates = Jinja2Templates(directory="templates")

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login-page")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register-page")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/tasks-page")
def tasks_page(request: Request):
    return templates.TemplateResponse("tasks.html", {"request": request})


app.include_router(users.router)
app.include_router(tasks.router)