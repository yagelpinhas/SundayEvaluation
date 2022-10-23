import json
import pymysql 
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="evaluation_db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def insert_to_diary(dairy_ingredient):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT INTO dairy (name) VALUES("{dairy_ingredient}");'
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)

def insert_to_gluten(gluten_ingredient):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT INTO gluten (name) VALUES("{gluten_ingredient}");'
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)

def insert_to_tables():
    dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
    gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]
    for dairy_ingredient in dairy_ingredients:
        insert_to_diary(dairy_ingredient)
    for gluten_ingredient in gluten_ingredients:
        insert_to_gluten(gluten_ingredient)

insert_to_tables()