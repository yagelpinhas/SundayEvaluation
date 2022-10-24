
const RecipeManager = function () {
    recipes=[]
    const getRecipes = async function(ingredient,gluten_free,dairy_free){
        recipes = await $.get(`/recipes?ingredient=${ingredient}&gluten_free=${gluten_free}&dairy_free=${dairy_free}`)
        return recipes
    }

    const getRecipeIngredients = function(title){
        ingredients=[]
        let relevant_recipe;
        for (recipe of recipes){

            if(recipe["title"]==title){
                relevant_recipe =recipe["ingredients"]
            }
        }
        for (ingredient of relevant_recipe){
            ingredients.push({"ingredient" : ingredient})
        }
        return ingredients
    }

    const getFirstIngredient = function(title){
        return getRecipeIngredients(title)[0]["ingredient"]
    }

    return {
        getRecipes: getRecipes,
        getRecipeIngredients: getRecipeIngredients,
        getFirstIngredient: getFirstIngredient
    }
}
