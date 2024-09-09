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
    collection = database.mycol
    k = collection.find_one({"ArtId":int(idi)})
    print(k)
    photolink = k['URL']
    photolink=photolink.split('html')
    photolink = photolink[0]+'art'+photolink[1]+'jpg'


    if k:        
        data = {"id":idi,
         "type":k['TECHNIQUE'],
         "date":k['TIMEFRAME'],
    "photo":photolink,
    "title":k['TITLE'],
    "artist":k['AUTHOR'],
    "origin":k['LOCATION'],

    "details":'hello world'}


        
        return templates.TemplateResponse("art.html", {"request": request,"Data":data})
    return 'not found'



