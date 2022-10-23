from tkinter.tix import Tree
from fastapi import FastAPI , status ,  HTTPException , Request , Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import requests
import pymysql 
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

def check_ingredient(ingredient,table_name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM {table_name} WHERE name ="{ingredient}";'
            cursor.execute(query)
            result = cursor.fetchall()
            if(len(result)==0):
                return False
            else:
                return True
    except TypeError as e:
        print(e)

def filter_recipe(recipe,table_name):
    for ingredient in recipe["ingredients"]:
        if check_ingredient(ingredient,table_name)==True:
            return False
    return True

def filter_attributes(recipes):
    filtered_recipes_by_attributes=[]
    for recipe in recipes:
        filtered_recipes_by_attributes.append({"ingredients":recipe["ingredients"],"title":recipe["title"],"thumbnail": recipe["thumbnail"],"href":recipe["href"]})
    return filtered_recipes_by_attributes

@app.get('/recipes/')
def get_recipes(ingredient,gluten_free,dairy_free):
    res = requests.get(f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}")
    recipes=res.json()["results"]
    if gluten_free=="true":
        recipes = list(filter(lambda recipe: (filter_recipe(recipe,"gluten")), recipes))
    if dairy_free=="true":
        recipes = list(filter(lambda recipe: (filter_recipe(recipe,"dairy")), recipes))
    recipes = filter_attributes(recipes)
    return recipes

@app.get('/')
def root():
    return FileResponse('./client/index.html')

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8046,reload=True)