$( document ).ready(function() {
    $('.nav-tabs a:first').tab('show');
    $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });

    /// calculate formula
    $('.index input').focusout(function(){
        $( "input[type='text']" ).each(function( index ) {
            eval($(this).attr('id') + " = parseFloat($('#"+ $(this).attr('id')+"').val());");
        });
        
        $( "input" ).each(function( index ) {
            //console.log( index + ": " + $( this ).text() );
            if ($(this).data('formula')){
                $(this).val(eval($(this).data('formula')));
            }
        });
    });

});