var toolbar = [
            ['style', ['style', 'bold', 'italic', 'underline', 'strikethrough', 'clear']],
            ['fonts', ['fontsize', 'fontname']],
            ['color', ['color']],
            ['undo', ['undo', 'redo', 'help']],
            ['ckMedia', ['ckImageUploader', 'ckVideoEmbeeder']],
            ['misc', ['link', 'picture', 'table', 'hr', 'codeview', 'fullscreen']],
            ['para', ['ul', 'ol', 'paragraph', 'leftButton', 'centerButton', 'rightButton', 'justifyButton', 'outdentButton', 'indentButton']],
            ['height', ['lineheight']],
        ];
cargarListaPatrones();

$('#oa-paso1').on('submit', function(event){
    event.preventDefault();
    var oaTitulo = $("#oatitulo").val();
    var oaDescripcion = $("#oadescripcion").val();
    var oaPatron = $("#oapatron").val();
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "paso1/", // the endpoint
        type : "POST", // http method
        data : { titulo : oaTitulo, descripcion : oaDescripcion, patron : oaPatron, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#oaid").val(data.oaid);
            $("#btnTab1").removeClass('disabled');
            $("#btnGuardarPaso1").removeClass('red');
            $("#btnGuardarPaso1").addClass('green');
            $("#btnGuardarPaso1").html('Guardado');
            cargarSeccionesPatron(oaPatron);
            
            Materialize.toast('Objeto guardado con exito!!', 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded')
        }
    });
});

$('#oa-paso2').on('submit', function(event){
    event.preventDefault();
    var oaIntroduccion = $("#introduccion-oa").code();
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso2" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "paso2/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId, introduccion : oaIntroduccion, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#oaid").val(data.oaid);
            Materialize.toast('Objeto guardado con exito!!', 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded');
        }
    });
});

function cargarListaPatrones(){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "traerPatrones/", // the endpoint
        type : "POST", // http method
        data : { csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            data.forEach(function(patron) {
                $("#oapatron").append("<option value='"+patron.pk+"'>"+patron.fields.nombre+"</option>");
            });
            $("#oapatron").material_select();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar los patrones pedagogicos', 3000, 'rounded')
        }
    });
}

function cambiarTab(tabContentId,tabId){
    $("#"+tabId).removeClass("disabled");
    $('ul.tabs').tabs('select_tab', tabContentId);
}

function cargarSeccionesPatron(patronId){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "traerSeccionesPatron/", // the endpoint
        type : "POST", // http method
        data : { patron : patronId, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            data.forEach(function(seccion) {
                $("#oa-paso3").html();
                $("#oa-paso3").append("<h3>"+seccion.fields.nombre+"</h3>"+
                "<div class='row'>"+
                    "<div class='input-field col s12'>"+
                        "<div class='editor seccion' id='seccion"+seccion.pk+"'>"+
                        "</div>"+
                    "</div>"+
                "</div>");
            });
            $('.editor.seccion').materialnote({
                toolbar: toolbar,
                height: 100,
                minHeight: 100,
                defaultBackColor: '#fff'
            });
            Materialize.toast('Secciones con exito!!', 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}



