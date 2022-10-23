const source = $(`#recipes-template`).html()
const template = Handlebars.compile(source)

const Renderer = function() {
    const render=function(recipes){
        const newHTML = template({recipes})
        $(`#recipesBoard`).empty().append(newHTML)
    }
    const renderIngredients = function(ingredients,recipe){
        const sourceIngredients = $(`.ingredients-template`).html()
        const templateIngredients = Handlebars.compile(sourceIngredients)
        const newHTML = templateIngredients({ingredients})
        recipe.find(".dropup-content").append(newHTML)
    }
    return {
        render: render,
        renderIngredients: renderIngredients
    }
}