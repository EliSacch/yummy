$(document).ready(function () {

    /* Materialize CSS Inizialization */
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('select').formSelect();
    $('.tooltipped').tooltip();


    /* Custom JS */
    $('.go-back').click(function () {
        window.history.back();
    });


    /**
     * This function is used to add a new ingredient to the recipe.
     * It is called when the user clicks on the "Add Ingredient" button.
     * */
    var ingredients = [];

    $('#add-ingredient-btn').click(function () {
        // First we get the values from the input fields
        const ingredient_name = $('#ingredient-name').val();
        const amount = $('#amount').val();
        const unit = $('#unit').val();

        // Then we check if the input fields are empty. The unit is not mandatory.
        if (ingredient_name == '') {
            $('#ingredient-name').addClass('invalid');
            $('#ingredient-name').focus();
        } else if (amount == '') {
            $('#amount').addClass('invalid');
            $('#amount').focus();
        } else {
            // If the input fields are not empty, we remove the invalid class and the active class from the label
            $('#ingredient-name').removeClass('invalid');
            $('#ingredient-name').next().removeClass('active');
            $('#amount').removeClass('invalid');
            $('#amount').next().removeClass('active');
            $('#unit').next().removeClass('active');

            // Then we add the ingredient to the ingredients array
            ingredients.push({ 'name': ingredient_name, 'amount': amount, 'unit': unit });
            show_added_ingredients(ingredients);

            // Finally we clear the input fields
            $('#ingredient-name').val('');
            $('#amount').val('');
            $('#unit').val('');
        }

        // We add the event listeners to the input fields, so that when the user changes the value, the invalid class is removed
        $('#ingredient-name').change(function() {
            $('#ingredient-name').removeClass('invalid');
        });

        $('#amount').change(function() {
            $('#amount').removeClass('invalid');
        });
    });
});


/**
 * This function is used to show the added ingredients from the ingredients array.
 * It also adds the event listener to the remove-ingredient button, 
 * so that when the user clicks on it, the ingredient is removed from the array.
 * @param {ARRAY of Objects} ingredients 
 */
function show_added_ingredients(ingredients) {
    // First we empty the ingredients-list div, so that we don't have duplicates
    $('#ingredients-list').empty();
    // Then we loop through the ingredients array and append a div for each ingredient
    for (var i = 0; i < ingredients.length; i++) {
        var ingredient_line = `
    <div class="ingredient-line">
        <div>
            <a class="tooltipped" data-position="bottom" data-tooltip="Remove Ingredient">
                <button type="button" class="remove-ingredient btn-floating" data-index="${i}">
                    <i class="small material-icons">remove</i>
                </button>
            </a>
        </div>
        <div>
            ${ingredients[i].name}: ${ingredients[i].amount} ${ingredients[i].unit} 
        </div>
    </div>`;
        $('#ingredients-list').append(ingredient_line);
    }

    // We initialize the tooltips
    $('.tooltipped').tooltip();

    // Finally we add the event listener to the remove-ingredient button
    $('.remove-ingredient').click(function () {
        index = $(this).data('index');
        remove_ingredient(ingredients, index);
    });

    // We also add the ingredients array to the hidden input field
    ingredients_JSON = JSON.stringify(ingredients.join(','));
    $('#ingredients').val(ingredients_JSON);
}


/**
 * This function is used to remove an ingredient from the ingredients array.
 * It is called when the user clicks on the remove-ingredient button.
 * It takes the index of the ingredient to be removed and removes it from the array.
 * Then it calls the function show_added_ingredients to show the updated ingredients.
 * @param {ARRAY of Objects} ingredients 
 * @param {Integer} index 
 */
function remove_ingredient(ingredients, index) {
    ingredients.splice(index, 1);
    show_added_ingredients(ingredients);
}
