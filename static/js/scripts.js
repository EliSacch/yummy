$(document).ready(function(){
    
    /* Materialize CSS Inizialization */
    $('.sidenav').sidenav();
    $('.modal').modal();


    /* Custom JS */
    $('.go-back').click(function(){
        window.history.back();
    });

  });