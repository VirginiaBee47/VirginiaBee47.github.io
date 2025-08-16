from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
app.mount("/styles", StaticFiles(directory="styles"), name="styles")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    data = {"message": "test"}

    return templates.TemplateResponse("index.html", {"request": request, **data})

@app.get("/music", response_class=HTMLResponse)
async def music(request: Request):
    data = {"message": "Music"}

    return templates.TemplateResponse("music.html", {"request": request, **data})

@app.get("/scrab", response_class=HTMLResponse)
async def scrab(request: Request):
    data = {}

    return templates.TemplateResponse("scrab.html", {"request": request, **data})
