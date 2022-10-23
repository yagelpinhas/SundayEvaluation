
const RecipeManager = function () {
    recipes=[]
    const getRecipes = async function(ingredient,gluten_free,dairy_free){
        recipes = await $.get(`/recipes?ingredient=${ingredient}&gluten_free=${gluten_free}&dairy_free=${dairy_free}`)
        return recipes
    }

    const getRecipeIngredients = function(title){
        ingredients=[]
        for (recipe of recipes){
            if(recipe["title"]==title){
                relevant_recipt =recipe["ingredients"]
            }
        }
        for (recipe of relevant_recipt){
            ingredients.push({"ingredient" : recipe})
        }
        return ingredients
    }

    return {
        getRecipes: getRecipes,
        getRecipeIngredients: getRecipeIngredients
    }
}
