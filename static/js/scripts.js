$(document).ready(function(){
    
    /* Materialize CSS Inizialization */
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('select').formSelect();


    /* Custom JS */
    $('.go-back').click(function(){
        window.history.back();
    });


    var ingredients = [];

    $('#add-ingredient-btn').click(function(){

        const ingredient_name = $('#ingredient-name').val();
        const amount = $('#amount').val();
        const unit = $('#unit').val();

        ingredients.push({'name': ingredient_name, 'amount' : amount, 'unit': unit});
        show_added_ingredients(ingredients);

        $('#ingredient-name').val('');
        $('#amount').val('');
        $('#unit').val('');

    });

  });

  function show_added_ingredients(ingredients){
    $('#ingredients-list').empty();
    for(var i = 0; i < ingredients.length; i++) {
        var ingredient_line = `
        <div class="ingredient-line row">
            <div class="col s1">
                <button type="button" class="remove-ingredient btn-floating" data-index="${i}">
                    <i class="small material-icons">remove</i>
                </button>
            </div>
            <div class="col s11">
                ${ingredients[i].name}: ${ingredients[i].amount} ${ingredients[i].unit} 
            </div>
        </div>`;
        $('#ingredients-list').append(ingredient_line);
    }

    $('.remove-ingredient').click(function(){
        index = $(this).data('index');
        remove_ingredient(ingredients, index);
    });
 }
 
 function remove_ingredient(ingredients, index){
    ingredients.splice(index, 1);
    show_added_ingredients(ingredients);
}
