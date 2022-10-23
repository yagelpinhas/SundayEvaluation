
const renderer = Renderer()
const recipe_manager = RecipeManager()

const fetch = async function () {
    let ingredient = $(`#recipeInput`).val()
    let gluten_free="false";
    let dairy_free="false";
    if(document.getElementById('glutenCheckBox').checked) {
      gluten_free="true";
    } 
    if(document.getElementById('dairyCheckBox').checked) {
      dairy_free="true";
    }
    recipes = await recipe_manager.getRecipes(ingredient,gluten_free,dairy_free)
    renderer.render(recipes)
}

$("body").on("click",".ingredients", async function(){
  let recipe = $(this).closest(".recipe")
  let title = recipe.find(".title").html()
  ingredients = recipe_manager.getRecipeIngredients(title)
  renderer.renderIngredients(ingredients,recipe)
})

$("body").on("click",".img", async function(){
  let recipe = $(this).closest(".recipe")
  let title = recipe.find(".title").html()
  let first_ingredient = recipe_manager.getFirstIngredient(title)
  alert(`${first_ingredient}`);
})

