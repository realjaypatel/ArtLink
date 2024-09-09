from starlette import status
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status
import json
import database
templates = Jinja2Templates(directory="templates")


router = APIRouter(
    # prefix='/',
    tags=['home']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def return_home(request: Request):
    art_list = []
    collection = database.mycol
    a = collection.aggregate([ 
    { '$match': { 'TECHNIQUE': {"$regex" : 'Oil on canvas'} } },
    { '$sample': { 'size': 10 }}])
    b = collection.aggregate([ 
    { '$match': { 'TECHNIQUE': {"$regex" : 'Stone'} } },
    { '$sample': { 'size': 10}}])

    for value in a:
        photolink = value['URL']
        photolink=photolink.split('html')
        photolink = photolink[0]+'detail'+photolink[1]+'jpg'
        print(value)

        data = {"id":value['ArtId'],
             "type":value['TECHNIQUE'],
             "date":value['TIMEFRAME'],
            "photo":photolink,
            "title":value['TITLE'],
            "artist":value['AUTHOR'],
            "origin":value['LOCATION'],
            "details":'hello world'}
        art_list.append(data)


    for value in b:
        photolink = value['URL']
        photolink=photolink.split('html')
        photolink = photolink[0]+'detail'+photolink[1]+'jpg'
        print(value)

        data = {"id":value['ArtId'],
             "type":value['TECHNIQUE'],
             "date":value['TIMEFRAME'],
            "photo":photolink,
            "title":value['TITLE'],
            "artist":value['AUTHOR'],
            "origin":value['LOCATION'],
            "details":'hello world'}
        art_list.append(data)
    


    return templates.TemplateResponse("home.html", {"request": request,"Data":art_list})

