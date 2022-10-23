
const renderer = Renderer()
const module = RecipeManager()

const fetch = async function () {
    const ingredient = $(`#recipeInput`).val()
    let gluten_free="false";
    let dairy_free="false";
    if(document.getElementById('glutenCheckBox').checked) {
      gluten_free="true";
    } 
    if(document.getElementById('dairyCheckBox').checked) {
      dairy_free="true";
    }
}

