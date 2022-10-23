
const RecipeManager = function () {
    const getRecipes = async function(ingredient,gluten_free,dairy_free){
        return $.get(`/recipes?ingredient=${ingredient}&gluten_free=${gluten_free}&dairy_free=${dairy_free}`)
    }

    return {
        getRecipes: getRecipes
    }
}
