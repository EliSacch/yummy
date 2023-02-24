$(document).ready(function(){
    
    /* Materialize CSS Inizialization */
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('select').formSelect();


    /* Custom JS */
    $('.go-back').click(function(){
        window.history.back();
    });

  });