var ret_dict = function(text_cells, value_cells){
    text_cells = text_cells.split(':');
    var i1 = text_cells[0].substring(1);
    var i2 = text_cells[1].substring(1);
    console.log(i1);
    console.log(i2);
    var text_col = text_cells[0][0];
    var value_col = value_cells[0][0];
    var text_dict = {};
    for(i=parseInt(i1); i<= parseInt(i2); i++){
        if ($('#' + text_col + i ).val()){
            text_dict[$('#' + text_col + i ).val()] = $('#' + value_col + i ).val();
        }
    }
    //console.log(text_dict);
    return text_dict;
}

var lookup = function(value, text_cells, value_cells){
    return ret_dict(text_cells, value_cells)[value];
}

var lookup_c = function(input, text_cells, value_cells){
    
    var text_dict = ret_dict(text_cells, value_cells);

    console.log(text_dict);
    var selectbox_str = "<select id='"+ input +"' style='width:100%;'>";
    for (item in text_dict){
        selectbox_str += '<option value="' + text_dict[item] +'">' + item + "</option>";
    }
    selectbox_str += "</select>"
    var nearest_td = $('#'+input).closest("td");
    nearest_td.empty();
    nearest_td.html(selectbox_str);
}

$( document ).ready(function() {
    $('.nav-tabs a:first').tab('show');
    $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });

    var execution = function(){
        $( ".index input[type='text'],.index select" ).each(function( index ) {
            eval($(this).attr('id') + " = $('#"+ $(this).attr('id')+"').val();");
        });

        $( ".index input , .index select" ).each(function( index ) {
            //console.log( index + ": " + $( this ).text() );
            if ($(this).data('formula')){
                var formula = $(this).data('formula');
                $(this).val(eval(formula));
            }
        });
    }
    execution();
    execution();
    /// calculate formula
    $('.index .sheet1 input').focusout(function(){
        execution();
    });

    $('.index select').change(function(){
        execution();
    });

});