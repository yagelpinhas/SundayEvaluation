const source = $(`#recipes-template`).html()
const template = Handlebars.compile(source)

const Renderer = function() {
    const render=function(recipes){
        const newHTML = template({recipes})
        $(`#recipesBoard`).empty().append(newHTML)
    }
    return {
        render: render
    }
}