import pymysql 
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="evaluation_db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

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