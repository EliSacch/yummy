$(document).ready(function(){
    
    /* Materialize CSS Inizialization */
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('select').formSelect();


    /* Custom JS */
    $('.go-back').click(function(){
        window.history.back();
    });


    $('#add-ingredient-btn').click(function(){
        var ingredients = []
        var ingredient_name = $('#ingredient-name').val();
        var amount = $('#amount').val();
        var unit = $('#unit').val();

        var ingredient_line = '<div class="ingredient-line row">'
        +'<div class="col s1"><button class="remove-ingredient btn-floating">'
        +'<i class="small material-icons">remove</i>'
        +'</button></div>'
        +'<div class="col s11">' 
        + ingredient_name + ': ' 
        + amount + ' ' 
        + unit 
        + '</div></div>';

        $('#ingredients-list').append(ingredient_line);
        $('#ingredient-name').val('');
        $('#amount').val('');
        $('#unit').val('');
        ingredients.push({'name': ingredient_name, 'amount' : amount, 'unit': unit});
        for(ingredient of ingredients) {
            console.log(ingredient.name, ingredient.amount, ingredient.unit)
        }
    });

  });