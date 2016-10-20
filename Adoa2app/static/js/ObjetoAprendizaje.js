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
cargarDatosGuardados();

$('#oa-paso1').on('submit', function(event){
    event.preventDefault();
    var oaId = $("#oaid").val();
    var oaTitulo = $("#oatitulo").val();
    var oaDescripcion = $("#oadescripcion").val();
    var oaPatron = $("#oapatron").val();
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/Paso1/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId,titulo : oaTitulo, descripcion : oaDescripcion, patron : oaPatron, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#oaid").val(data.oaid);
            $("#evaluacionid").val(data.evaluacionid);
            $("#btnTab1").removeClass('disabled');
            $("#btnGuardarPaso1").removeClass('red');
            $("#btnGuardarPaso1").addClass('green');
            $("#btnGuardarPaso1").html('Editar');
            cargarSeccionesPatron(oaPatron);
            $(".tab").removeClass("disabled");
            
            Materialize.toast(data.result, 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded')
        }
    });
});

$('#btnGuardarPaso2').on('click', function(){
    var oaIntroduccion = $("#introduccion-oa").code();
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso2" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/Paso2/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId, introduccion : oaIntroduccion, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            Materialize.toast('Guardado con exito!!', 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded');
        }
    });
});

$('#btnGuardarPaso3').on('click', function(){
    var secciones = [];
    $(".editor.seccion").each(function() {
        var idSeccion = $(this).data("id");
        var contenidoSeccion = $("#seccion"+idSeccion).code();
        secciones.push({ 
            "id" : idSeccion,
            "contenido"  : contenidoSeccion
        });
    });
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/Paso3/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId, secciones : JSON.stringify(secciones), csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            Materialize.toast(data.result, 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded');
        }
    });
});

function cargarListaPatrones(){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerPatrones/", // the endpoint
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
        url : "/CrearOA/TraerSeccionesPatron/", // the endpoint
        type : "POST", // http method
        data : { patron : patronId, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#oa-secciones").html('');
            data.forEach(function(seccion) {
                $("#oa-secciones").append("<h3>"+seccion.fields.nombre+"</h3>"+
                "<div class='row'>"+
                    "<div class='input-field col s12'>"+
                        "<div class='editor seccion' data-id='"+seccion.pk+"' id='seccion"+seccion.pk+"'>"+
                        "</div>"+
                    "</div>"+
                "</div>");
            });
            $('.editor.seccion').materialnote({
                toolbar: toolbar,
                height: 300,
                minHeight: 100,
                defaultBackColor: '#fff'
            });
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}

function cargarDatosGuardados(){

    var oaId = $("#editoa").val();
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerDatosObjeto/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
        var terminos = JSON.parse(data.terminos);
            $("#oaid").val(data.oaid);
            $("#evaluacionid").val(data.evaluacionid);
            $("#btnTab1").removeClass('disabled');
            $("#btnGuardarPaso1").removeClass('red');
            $("#btnGuardarPaso1").addClass('green');
            $("#btnGuardarPaso1").html('Editar');
            //cargarSeccionesPatron(oaPatron);
            $(".tab").removeClass("disabled");
            
            Materialize.toast("Patron cargado con exito", 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded')
        }
    });
}


