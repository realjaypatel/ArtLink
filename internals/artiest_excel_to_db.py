import pandas as pd
import pymongo
myArts = pymongo.MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/ArtDB")
mydb = myArts["ArtDB"]
mycol= mydb["Art"]


data = pd.read_excel('internals\catalog.xlsx')
data['username'] = data['URL'].str.split('/', n=6, expand=False)
data['username'] = data['username'].apply(lambda x: x[5])
# dataitems = ['AUTHOR','BORN-DIED','TITLE','DATE','TECHNIQUE','LOCATION','URL','FORM','TYPE','SCHOOL','TIMEFRAME']

data = data.to_dict('records')

num = 1
for values in data:
    values['ArtId'] = num
    num+=1
    x = mycol.insert_one(values)
    print(num,values['username'])







# id->'achenbac'
# ACHENBACH, Oswald
# (b. 1827, Düsseldorf, d. 1905, Düsseldorf)
# painter
# German
# https://www.wga.hu/bio/a/achenbac/biograph.html
# https://www.wga.hu/biojpg/a/achenbac/biograph.jpg



# mongodb+srv://<db_username>:<db_password>@cluster0.u3fdtma.mongodb.net/ArtDB
# export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# import requests
# from bs4 import BeautifulSoup

# def return_bio(url):
#     r = requests.get('https://www.wga.hu/bio/l/leonardo/biograph.html')
#     soup = BeautifulSoup(r.content, 'html.parser')
#     soup = soup.find('p')
#     return soup
