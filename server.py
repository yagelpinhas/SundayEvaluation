from tkinter.tix import Tree
from fastapi import FastAPI , status ,  HTTPException , Request , Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import requests
import pymysql
import helper_methods as helper 
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="evaluation_db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

app = FastAPI()
app.mount("/client", StaticFiles(directory="client"), name="client")

@app.get('/sanity')
def sanity():
    return "OK"

@app.get('/recipes/')
def get_recipes(ingredient,gluten_free,dairy_free, response: Response):
    res = requests.get(f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}")
    recipes=res.json()["results"]
    if len(recipes)==0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": "No recipes containing this ingredient unfortunately"}
    if gluten_free=="true":
        recipes = list(filter(lambda recipe: (helper.filter_recipe(recipe,"gluten")), recipes))
    if dairy_free=="true":
        recipes = list(filter(lambda recipe: (helper.filter_recipe(recipe,"dairy")), recipes))
    recipes = helper.filter_attributes(recipes)
    return recipes
    a=5

@app.get('/')
def root():
    return FileResponse('./client/index.html')

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8076,reload=True)