from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
import json
import database
templates = Jinja2Templates(directory="templates")


router = APIRouter(
    prefix='/paintings',
    tags=['paintings']
)






@router.get('/', status_code=status.HTTP_200_OK)
async def return_home(request: Request):
    return templates.TemplateResponse("paintings.html", {"request": request,"data":database})


