function crearActividad() {
    var idTipoActividad= $("#actividadesSelect").val();
    
    switch(idTipoActividad) {
    case "1":
        Materialize.toast('Actividad 1 seleccionada', 3000, 'rounded');
        crearVerdaderoFalso();
        break;
    case "2":
        Materialize.toast('Actividad 2 Seleccionada', 3000, 'rounded');
        crearAsociacion();
        break;
    case "3":
        Materialize.toast('Actividad 3 Seleccionada', 3000, 'rounded');
        crearVideo();
        break;
    case "4":
        Materialize.toast('Actividad 4 Seleccionada', 3000, 'rounded');
        crearOrdenamiento();
        break;
    case "5":
        Materialize.toast('Actividad 5 Seleccionada', 3000, 'rounded');
        crearIdentificacion();
        break;
    default:
        Materialize.toast('Ninguna Actividad Seleccionada', 3000, 'rounded');
    }

}

function crearVerdaderoFalso(){
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "CrearVerdaderoFalso/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            var idActividad = data.verdaderoFalsoId;
            $("#actividades").show();
            $("#listaactividades").append(
            "<li id='actividad"+idActividad+"' class='collection-item'><div>Verdadero o Falso"+
            "<a onclick='eliminarVerdaderoFalso("+idActividad+")' href='#!' class='secondary-content'><i class='material-icons'>delete</i></a>"+
            "<a onclick='modalEditarVerdaderoFalso("+idActividad+")' href='#!' class='secondary-content'><i class='material-icons'>mode_edit</i></a>"+
            "<a onclick='verVerdaderoFalso("+idActividad+")' href='#!' class='secondary-content'><i class='material-icons'>visibility</i></a>"+
            "</div></li>"
            );
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al crear actividad', 3000, 'rounded')
        }
    });
}

function modalEditarVerdaderoFalso(idActividad){
    $('#modalEditarActividadContenido').html('');
    $('#modalEditarActividadContenido').append(
        "<div class='input-field col s12'>"+
            "<textarea id='verdaderoFalsoEnunciado' name='verdaderoFalsoEnunciado' class='materialize-textarea'></textarea>"+
            "<label for='verdaderoFalsoEnunciado'>Enuncuado</label>"+
        "</div>"+
        "<div id='actividadContenido'></div>"+
        "<div class='row col s12'>"+
            "<button id='btnAgregarTermino' class='btn waves-effect waves-light red left' onclick='agregarTerminoVerdaderoFalso()'><i class='material-icons left'></i>Agregar Termino</button>"+
        "</div>"
    );
    $("#btnGuardarActividad").attr("onclick","guardarVerdaderoFalso("+idActividad+")");
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "TraerTerminosVerdaderoFalso/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            if(data.enunciado !==''){
                $("#verdaderoFalsoEnunciado").val(data.enunciado);
            }
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#actividadContenido").append(
                    "<div class='row termino'>"+
                        "<div class='input-field col s7'>"+
                            "<textarea name='afirmacion' class='materialize-textarea afirmacion'>"+termino.fields.afirmacion+"</textarea>"+
                            "<label for='Afirmacion'>Afirmacion</label>"+
                        "</div>"+
                        "<div class='input-field col s3'>"+
                            "<select class='respuesta' name='respuesta'>"+
                                "<option value='0' >Falso</option>"+
                                "<option value='1' >Verdadero</option>"+
                            "</select>"+
                            "<label>Respuesta</label>"+
                        "</div>"+
                        "<div class='row col s2'>"+
                            "<a class='btn-floating btn-large waves-effect waves-light red right' onclick='eliminarTermino(this)'><i class='material-icons'>delete</i></a>"+
                        "</div>"+
                    "</div>"
                    );
                });
            }
            $('select').material_select();
            $('#modalEditarActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}

function agregarTerminoVerdaderoFalso(){
    $('#actividadContenido').append(
        "<div class='row termino'>"+
            "<div class='input-field col s7'>"+
                "<textarea name='afirmacion' class='materialize-textarea afirmacion'></textarea>"+
                "<label for='Afirmacion'>Afirmacion</label>"+
            "</div>"+
            "<div class='input-field col s3'>"+
                "<select class='respuesta' name='respuesta'>"+
                    "<option value='0' >Falso</option>"+
                    "<option value='1' selected>Verdadero</option>"+
                "</select>"+
                "<label>Respuesta</label>"+
            "</div>"+
            "<div class='row col s2'>"+
                "<a class='btn-floating btn-large waves-effect waves-light red right' onclick='eliminarTermino(this)'><i class='material-icons'>delete</i></a>"+
            "</div>"+
        "</div>"
    );
    $('select').material_select();
}

function eliminarTermino(boton){
    $(boton).parent().parent().remove();
}

function guardarVerdaderoFalso(idActividad){
    var terminos = [];
    var enunciado = $("#verdaderoFalsoEnunciado").val();
    $(".row.termino").each(function() {
        var afirmacion = $(this).find( "textarea" ).val();
        var respuesta = $(this).find( "select" ).val();
        terminos.push({ 
            "afirmacion" : afirmacion,
            "respuesta"  : respuesta
        });
    });
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "GuardarVerdaderoFalso/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad,enunciado : enunciado, terminos : JSON.stringify(terminos), csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            Materialize.toast(data.result, 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded');
        }
    });
}

