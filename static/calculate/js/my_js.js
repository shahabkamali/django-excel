var lookup = function(value, text_cells, value_cells){
    text_cells = text_cells.split(':');
    var i1 = text_cells[0].substring(1);
    var i2 = text_cells[1].substring(1);
    //console.log(i1);
    //console.log(i2);
    var text_col = text_cells[0][0];
    var value_col = value_cells[0][0];
    var text_dict = {};
    for(i=i1; i<= i2; i++){
        text_dict[$('#' + text_col + i ).val()] = $('#' + value_col + i ).val();
    }
    //console.log(text_dict);
    return text_dict[value];
}
$( document ).ready(function() {
    $('.nav-tabs a:first').tab('show');
    $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });

    /// calculate formula
    $('.index .sheet1 input').focusout(function(){
        $( "input[type='text']" ).each(function( index ) {
            eval($(this).attr('id') + " = $('#"+ $(this).attr('id')+"').val();");
        });
        
        $( "input" ).each(function( index ) {
            //console.log( index + ": " + $( this ).text() );
            if ($(this).data('formula')){
                var formula = $(this).data('formula');
                // formula = formula.replace("/^[A-Z]",'B');
                // console.log(formula);
                $(this).val(eval(formula));
            }
        });
    });
    
    


});