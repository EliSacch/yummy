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
     * We add an event listener to the tags field.
     */
    $('#id_tags').on('keyup', display_tags);


    /**
     * We add an event listener to hours and minutes field.
     */
    $('#hours').on('input', set_prepration_time);
    $('#minutes').on('input', set_prepration_time);

    /* We call the random_icon function to create random food icons */
    random_icon();

    /* We add an event listener to the remove-ingredient buttons */
    if ($('.remove-ingredient').length > 0) {
        $('.remove-ingredient').click(remove_ingredient_form);
    }

    /* Call the display message function to display any error/success message */
    display_message();

    $('.difficulty-choices li > label').click(function () {
        $(this).prev().prop('checked', true);
    });

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
     * This functions takes the string entered in the tags field and splits it into an array.
     * The array is displayed underneath the tags field, to show the valid tags.
     */
function display_tags() {
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
    
}

    function set_prepration_time() {
        const preparationTime = $('#id_preparation_time');
        const minutes = $('#minutes').val();
        const hours = $('#hours').val()

        let totalHours = 0 + Math.floor(minutes / 60);

        if (parseInt(hours) > 0) {
            totalHours = parseInt(hours);
        } 

        + Math.floor(minutes / 60);
        const remainingMinutes = minutes % 60;
        let time = {
            'hours': totalHours,
            'minutes': remainingMinutes
        };

        preparationTime.val(JSON.stringify(time));
    }


/**
 * Image placeholder animation.
 * This function is used to create random food icons and spread them around our image placeholder.
 */
const iconsNames = ['restaurant', 'cake', 'local_pizza', 'egg',
    'bakery_dining', 'icecream', 'local_cafe', 'local_bar', 'nutrition', 'ramen_dining'];
function random_icon() {
    for (let i = 0; i < 6; i++) {
        var randomIcon = iconsNames[Math.floor(Math.random() * iconsNames.length)];
        const iconHtml = `<span class="food-icon"><i class="material-icons">${randomIcon}</i></span>`;
        $('.food-icons-container').append(iconHtml);
    } 
    random_position();
}

function random_position() {
    const icons = $('.food-icon');
    for (let i = 0; i < icons.length; i++) {
        var top = Math.floor(Math.random() * 90);
        var left = Math.floor(Math.random() * 90);
        icons[i].style.top = `${top}%`;
        icons[i].style.left = `${left}%`;
    }
}


/**
 * This function is used to display the message content when there is any.
 */
function display_message() {
    const messageSection = $('#messages');
    const messageList = $('.messages-list');
    const isThereMessage = messageList.children().length > 0;

    if (isThereMessage) {
        messageSection.fadeIn('slow');
        setTimeout(function () {
            messageSection.fadeOut('slow');
        }, 5000);
    }
}