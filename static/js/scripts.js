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

    $('.go-home').click(function () {
        window.location.href = "/";
    });


    /**
     * This function is used to add a new ingredient to the recipe.
     * It is called when the user clicks on the "Add Ingredient" button.
     * */
    $('#add-ingredient-btn').click(add_ingredient_form);


    /**
     * This functions takes the string entered in the tags field and splits it into an array.
     * The array is displayed underneath the tags field, to show the valid tags.
     */
    $('#id_tags').on('keyup', function () {
        var tags = $('#id_tags').val();
        var tagsArray = tags.split(/[ ,#]+/);

        $('#valid-tags').empty();
        for(let tag of tagsArray) {
            // We check if the tag is empty, if so we skip it
            if(tag == '') {
                continue;
            } else {
                $('#valid-tags').append(`<span class="hashtag">#${tag}</span>`);
            }
        }
        
    });

    /* We call the random_icon function to create random food icons */
    random_icon();

    /* We add an event listener to the remove-ingredient buttons */
    if ($('.remove-ingredient').length > 0) {
        $('.remove-ingredient').click(remove_ingredient_form);
    }

});


/**
 * This function is used to add a new ingredients form.
 * The following code was taken from the "CodingEnterpreneur" tutorial on YouTube.
 * The link to the tutorial is: https://www.youtube.com/watch?v=s3T-w2jhDHE&t=1293s
 * The code has been modified to fit this project and to be used with JQuery.
 */
function add_ingredient_form() {
    const emptyFormCopy = $('#empty-form').clone();
    const ingredientsContainer = $('#ingredients-container');
    const totalForms = $('#id_ingredients-TOTAL_FORMS');
    const formCount = $('.ingredient-form').length;
    const regex = RegExp('__prefix__', 'g');
    
    let newFormCount = formCount;

    emptyFormCopy.removeClass('hidden').addClass('ingredient-form');
    
    totalForms.val(newFormCount + 1);
    emptyFormCopy.prop('id', `ingredient-form-${newFormCount}`);
    emptyFormCopy.html(emptyFormCopy.html().replace(regex, newFormCount));

    ingredientsContainer.append(emptyFormCopy);
    /* End of the code taken from the tutorial */

    /* Add event listener to the remove-ingredient button */
    $('.remove-ingredient').click(remove_ingredient_form);

}


/**
 * This function is used to remove an ingredient form.
 * It is called when the user clicks on the remove-ingredient button.
 */
function remove_ingredient_form() {
    const allForms = $('.ingredient-form');
    const parentDiv = $(this).parents('.ingredient-form');
    const index = allForms.index(parentDiv);
    const deleteForm = $(`#id_ingredients-${index}-DELETE`);
    if (allForms.length > 1) {
        deleteForm.val('on');
        deleteForm.prop('checked', true);
        parentDiv.hide();
    }
}


/**
 * Image placeholder animation.
 * This function is used to create random food icons and spread them around our image placeholder.
 */
const iconsNames = ['restaurant', 'cake', 'local_pizza', 'egg',
    'bakery_dining', 'icecream', 'local_cafe', 'local_bar', 'nutrition', 'ramen_dining'];
function random_icon() {
    for (let i = 0; i < 10; i++) {
        var randomIcon = iconsNames[Math.floor(Math.random() * iconsNames.length)];
        const iconHtml = `<span class="food-icon"><i class="material-icons">${randomIcon}</i></span>`;
        $('.food-icons-container').append(iconHtml);
    } 
    random_position();
}

function random_position() {
    const icons = $('.food-icon');
    for (let i = 0; i < icons.length; i++) {
        var top = Math.floor(Math.random() * 100);
        var left = Math.floor(Math.random() * 100);
        icons[i].style.top = `${top}%`;
        icons[i].style.left = `${left}%`;
    }
}