$( document ).ready(function() {
    $('#calc-btn').click(function(){
        var A = parseFloat($('#inputA').val());
        var B = parseFloat($('#inputB').val());
        var C = parseFloat($('#inputC').val());
        var D = parseFloat($('#inputD').val());
        var E = parseFloat($('#inputE').val());
        var F = parseFloat($('#inputF').val());
        $('#input-result').val(eval($('#input-formula').val()));

        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        var data ={
            A1 : A,
            A2 : B,
            A3 : C,
            A4 : D,
            A5 : E,
            A6 : F,
            'csrfmiddlewaretoken': csrftoken
        };
        $.ajax({
          method: "POST",
          url: "/calculation/ajax_req",
          data: data
        })
          .done(function( msg ) {
            alert( "Data Saved: " + msg );
          });
    });

});