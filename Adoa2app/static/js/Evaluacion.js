function agregarPreguntaEvaluacion(){
    $('#modalEditarPreguntaContenido').html('');
    $('#modalEditarPreguntaContenido').append(
    "<div class='input-field col s12'>"+
        "<input id='pregunta' name='pregunta' type='text' class='validate'>"+
        "<label for='pregunta' class=''>Pregunta</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input id='respuestacorrecta' name='respuestacorrecta' type='text' class='validate'>"+
        "<label for='respuestacorrecta' class=''>Respuesta Correcta</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input id='respuestaincorrecta1' name='respuestaincorrecta1' type='text' class='validate'>"+
        "<label for='respuestaincorrecta1' class=''>Respuesta Incorrecta 1</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input id='respuestaincorrecta2' name='respuestaincorrecta2' type='text' class='validate'>"+
        "<label for='respuestaincorrecta2' class=''>Respuesta Incorrecta 2</label>"+
    "</div>");
    $("#btnGuardarPregunta").attr("onclick","crearPregunta()");
    $('#modalEditarPregunta').openModal();
}


function crearPregunta(){
    var pregunta = $("#pregunta").val();
    var respuestacorrecta = $("#respuestacorrecta").val();
    var respuestaincorrecta1 = $("#respuestaincorrecta1").val();
    var respuestaincorrecta2 = $("#respuestaincorrecta2").val();

    var evaluacionId = $("#evaluacionid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "CrearPregunta/", // the endpoint
        type : "POST", // http method
        data : { evaluacionId : evaluacionId, pregunta : pregunta, respuestacorrecta : respuestacorrecta, respuestaincorrecta1 : respuestaincorrecta1, respuestaincorrecta2 : respuestaincorrecta2, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            var idPregunta = data.idPregunta;
            $("#preguntas").show();
            $("#listapreguntas").append(
            "<li id='pregunta"+idPregunta+"' class='collection-item'><div>"+pregunta+
            "<a onclick='eliminarPregunta("+idPregunta+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>delete</i></a>"+
            "<a onclick='modalEditarPregunta("+idPregunta+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>mode_edit</i></a>"+
            "</div></li>"
            );

            Materialize.toast(data.result, 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded');
        }
    });
}

function modalEditarPregunta(idPregunta){
    $('#modalEditarPreguntaContenido').html('');
    $('#modalEditarPreguntaContenido').append(
    "<div class='input-field col s12'>"+
        "<input id='pregunta' name='pregunta' type='text' class='validate'>"+
        "<label for='pregunta' class='active'>Pregunta</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input id='respuestacorrecta' name='respuestacorrecta' type='text' class='validate'>"+
        "<label for='respuestacorrecta' class='active'>Respuesta Correcta</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input id='respuestaincorrecta1' name='respuestaincorrecta1' type='text' class='validate'>"+
        "<label for='respuestaincorrecta1' class='active'>Respuesta Incorrecta 1</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input id='respuestaincorrecta2' name='respuestaincorrecta2' type='text' class='validate'>"+
        "<label for='respuestaincorrecta2' class='active'>Respuesta Incorrecta 2</label>"+
    "</div>");
    
    $("#btnGuardarPregunta").attr("onclick","guardarPregunta("+idPregunta+")");
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "TraerPregunta/", // the endpoint
        type : "POST", // http method
        data : { preguntaId : idPregunta, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            if(data.pregunta !==''){
                $("#pregunta").val(data.pregunta);
            }
            if(data.respuestacorrecta !==''){
                $("#respuestacorrecta").val(data.respuestacorrecta);
            }
            if(data.respuestaincorrecta1 !==''){
                $("#respuestaincorrecta1").val(data.respuestaincorrecta1);
            }
            if(data.respuestaincorrecta2 !==''){
                $("#respuestaincorrecta2").val(data.respuestaincorrecta2);
            }

            $('#modalEditarPregunta').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });

    $('#modalEditarPregunta').openModal();
}

function guardarPregunta(idPregunta){
    var pregunta = $("#pregunta").val();
    var respuestacorrecta = $("#respuestacorrecta").val();
    var respuestaincorrecta1 = $("#respuestaincorrecta1").val();
    var respuestaincorrecta2 = $("#respuestaincorrecta2").val();

    var evaluacionId = $("#evaluacionid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "GuardarPregunta/", // the endpoint
        type : "POST", // http method
        data : { preguntaId : idPregunta, pregunta : pregunta, respuestacorrecta : respuestacorrecta, respuestaincorrecta1 : respuestaincorrecta1, respuestaincorrecta2 : respuestaincorrecta2, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {

            Materialize.toast(data.result, 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded');
        }
    });
}

function eliminarPregunta(idPregunta){
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "EliminarPregunta/", // the endpoint
        type : "POST", // http method
        data : { preguntaId : idPregunta, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#pregunta"+idPregunta).remove();
            Materialize.toast(data.result, 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000, 'rounded');
        }
    });
}
