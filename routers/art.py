from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
import json
import database
templates = Jinja2Templates(directory="templates")


router = APIRouter(
    prefix='/art',
    tags=['art']
)



@router.get('/{idi}', status_code=status.HTTP_200_OK)
async def return_home(idi,request: Request):

    for dict in database.Data:
        
        if str(idi) == dict['id']:  
            return templates.TemplateResponse("art.html", {"request": request,"data":database})
    return 'not found'



