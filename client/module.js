
const RecipeManager = function () {
    recipes=[]
    const getRecipes = async function(ingredient,gluten_free,dairy_free){
        recipes = await $.get(`/recipes?ingredient=${ingredient}&gluten_free=${gluten_free}&dairy_free=${dairy_free}`)
        return recipes
    }

    return {
        getRecipes: getRecipes
    }
}
