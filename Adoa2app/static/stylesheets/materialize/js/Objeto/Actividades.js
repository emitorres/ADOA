function crearActividad() {
    var idTipoActividad= $("#actividadesSelect").val();
    
    switch(idTipoActividad) {
    case "1":
        crearVerdaderoFalso();
        break;
    case "2":
        crearAsociacion();
        break;
    case "3":
        crearVideo();
        break;
    case "4":
        crearOrdenamiento();
        break;
    case "5":
        crearIdentificacion();
        break;
    default:
        Materialize.toast('Ninguna Actividad Seleccionada', 3000);
    }

}

function crearVerdaderoFalso(){
    var oaId = $("#oaid").val();
    var nombreActividad = $("#nombreactividad").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/CrearVerdaderoFalso/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId,nombreactividad: nombreActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            var idActividad = data.verdaderoFalsoId;
            $("#actividades").show();
            $("#listaactividades").append(
             "<tr id='actividad"+idActividad+"'>"+
                "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                "<td>Verdadero o Falso</td>"+
                "<td>"+
                    "<button onclick='modalEditarVerdaderoFalso("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                    "<button id='btnVerActividad"+idActividad+"' onclick='verVerdaderoFalso("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left' disabled><i class='material-icons'>visibility</i></button>"+
                    "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                "</td>"+
              "</tr>"
            );
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al crear actividad', 3000)
        }
    });
}

function modalEditarVerdaderoFalso(idActividad){
    $('#modalEditarActividadContenido').html('');
    $('#modalEditarActividadContenido').append(
        "<div class='input-field col s12'>"+
            "<textarea id='verdaderoFalsoEnunciado' name='verdaderoFalsoEnunciado' class='materialize-textarea'></textarea>"+
            "<label class='active' for='verdaderoFalsoEnunciado'>Enunciado</label>"+
        "</div>"+
        "<div id='actividadContenido'></div>"+
        "<div class='row col s12'>"+
            "<button id='btnAgregarTermino' class='btn waves-effect waves-light red left' onclick='agregarTerminoVerdaderoFalso()'><i class='material-icons left'></i>Agregar Termino</button>"+
        "</div>"
    );
    $("#btnGuardarActividad").attr("onclick","guardarVerdaderoFalso("+idActividad+")");
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosVerdaderoFalso/", // the endpoint
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
                            "<label class='active' for='Afirmacion'>Afirmacion</label>"+
                        "</div>"+
                        "<div class='input-field col s3'>"+
                            "<select id='selectrespuesta-"+termino.pk+"' class='respuesta' name='respuesta'>"+
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
                    if(termino.fields.respuesta === true){
                        $("#selectrespuesta-"+termino.pk).val('1');
                    }else{
                        $("#selectrespuesta-"+termino.pk).val('0');
                    }
                    
                });
            }
            $('select').material_select();
            $('#modalEditarActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
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
        url : "/CrearOA/GuardarVerdaderoFalso/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad,enunciado : enunciado, terminos : JSON.stringify(terminos), csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#btnVerActividad"+idActividad).removeAttr('disabled');
            Materialize.toast(data.result, 3000)
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
        }
    });
}

function crearIdentificacion(){
    var oaId = $("#oaid").val();
    var nombreActividad = $("#nombreactividad").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/CrearIdentificacion/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId,nombreactividad: nombreActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            var idActividad = data.identificacionId;
            $("#actividades").show();
            $("#listaactividades").append(
             "<tr id='actividad"+idActividad+"'>"+
                "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                "<td>Identificacion</td>"+
                "<td>"+
                    "<button onclick='modalEditarIdentificacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                    "<button id='btnVerActividad"+idActividad+"' onclick='verIdentificacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left' disabled><i class='material-icons'>visibility</i></button>"+
                    "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                "</td>"+
              "</tr>"
            );
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al crear actividad', 3000)
        }
    });
}

function modalEditarIdentificacion(idActividad){
    $('#modalEditarActividadContenido').html('');
    $('#modalEditarActividadContenido').append(
        "<div class='input-field col s12'>"+
            "<textarea id='identificacionEnunciado' name='identificacionEnunciado' class='materialize-textarea'></textarea>"+
            "<label class='active' for='identificacionEnunciado'>Enunciado</label>"+
        "</div>"+
        "<div id='actividadContenido'></div>"+
        "<div class='row col s12'>"+
            "<button id='btnAgregarTermino' class='btn waves-effect waves-light red left' onclick='agregarTerminoIdentificacion()'><i class='material-icons left'></i>Agregar Termino</button>"+
        "</div>"
    );
    $("#btnGuardarActividad").attr("onclick","guardarIdentificacion("+idActividad+")");
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosIdentificacion/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            if(data.enunciado !==''){
                $("#identificacionEnunciado").val(data.enunciado);
            }
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#actividadContenido").append(
                    "<div class='row termino'>"+
                        "<div class='input-field col s7'>"+
                          "<input class='concepto' id='concepto-"+termino.pk+"' type='text'>"+
                          "<label for='concepto'  class='active'>Concepto</label>"+
                        "</div>"+
                        "<div class='input-field col s3'>"+
                            "<select id='selectrespuesta-"+termino.pk+"' class='respuesta' name='respuesta'>"+
                                "<option value='0' >No</option>"+
                                "<option value='1' >Si</option>"+
                            "</select>"+
                            "<label>Respuesta</label>"+
                        "</div>"+
                        "<div class='row col s2'>"+
                            "<a class='btn-floating btn-large waves-effect waves-light red right' onclick='eliminarTermino(this)'><i class='material-icons'>delete</i></a>"+
                        "</div>"+
                    "</div>"
                    );
                    if(termino.fields.respuesta === true){
                        $("#selectrespuesta-"+termino.pk).val('1');
                    }else{
                        $("#selectrespuesta-"+termino.pk).val('0');
                    }
                    $("#concepto-"+termino.pk).val(termino.fields.concepto);
                    
                });
            }
            $('select').material_select();
            $('#modalEditarActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function agregarTerminoIdentificacion(){
    $("#actividadContenido").append(
        "<div class='row termino'>"+
            "<div class='input-field col s7'>"+
              "<input class='concepto' type='text'>"+
              "<label for='concepto' class=''>Concepto</label>"+
            "</div>"+
            "<div class='input-field col s3'>"+
                "<select class='respuesta' name='respuesta'>"+
                    "<option value='0' >No</option>"+
                    "<option value='1' >Si</option>"+
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

function guardarIdentificacion(idActividad){
    var terminos = [];
    var enunciado = $("#identificacionEnunciado").val();
    $(".row.termino").each(function() {
        var concepto = $(this).find( "input.concepto" ).val();
        var respuesta = $(this).find( "select" ).val();
        terminos.push({ 
            "concepto" : concepto,
            "respuesta"  : respuesta
        });
    });
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/GuardarIdentificacion/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad,enunciado : enunciado, terminos : JSON.stringify(terminos), csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#btnVerActividad"+idActividad).removeAttr('disabled');
            Materialize.toast(data.result, 3000)
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
        }
    });
}

function crearOrdenamiento(){
    var oaId = $("#oaid").val();
    var nombreActividad = $("#nombreactividad").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/CrearOrdenamiento/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId,nombreactividad: nombreActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            var idActividad = data.ordenamientoId;
            $("#actividades").show();
            $("#listaactividades").append(
             "<tr id='actividad"+idActividad+"'>"+
                "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                "<td>Ordenamiento</td>"+
                "<td>"+
                    "<button onclick='modalEditarOrdenamiento("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                    "<button id='btnVerActividad"+idActividad+"' onclick='verOrdenamiento("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left' disabled><i class='material-icons'>visibility</i></button>"+
                    "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                "</td>"+
              "</tr>"
            );
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al crear actividad', 3000)
        }
    });
}

function modalEditarOrdenamiento(idActividad){
    $('#modalEditarActividadContenido').html('');
    $('#modalEditarActividadContenido').append(
        "<div class='input-field col s12'>"+
            "<textarea id='ordenamientoEnunciado' name='ordenamientoEnunciado' class='materialize-textarea'></textarea>"+
            "<label class='active' for='ordenamientoEnunciado'>Enunciado</label>"+
        "</div>"+
        "<div id='actividadContenido'></div>"+
        "<div class='row col s12'>"+
            "<button id='btnAgregarTermino' class='btn waves-effect waves-light red left' onclick='agregarTerminoOrdenamiento()'><i class='material-icons left'></i>Agregar Termino</button>"+
        "</div>"
    );
    $("#btnGuardarActividad").attr("onclick","guardarOrdenamiento("+idActividad+")");
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosOrdenamiento/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            if(data.enunciado !==''){
                $("#ordenamientoEnunciado").val(data.enunciado);
            }
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#actividadContenido").append(
                    "<div class='row termino'>"+
                        "<div class='input-field col s7'>"+
                            "<textarea name='texto' class='materialize-textarea texto'>"+termino.fields.texto+"</textarea>"+
                            "<label class='active' for='Texto'>Texto</label>"+
                        "</div>"+
                        "<div class='input-field col s3'>"+
                            "<select id='selectorden-"+termino.pk+"' class='orden' name='orden'>"+
                                "<option value='1'>1</option>"+
                                "<option value='2'>2</option>"+
                                "<option value='3'>3</option>"+
                                "<option value='4'>4</option>"+
                                "<option value='5'>5</option>"+
                                "<option value='6'>6</option>"+
                                "<option value='7'>7</option>"+
                                "<option value='8'>8</option>"+
                                "<option value='9'>9</option>"+
                                "<option value='10'>10</option>"+
                            "</select>"+
                            "<label>Orden</label>"+
                        "</div>"+
                        "<div class='row col s2'>"+
                            "<a class='btn-floating btn-large waves-effect waves-light red right' onclick='eliminarTermino(this)'><i class='material-icons'>delete</i></a>"+
                        "</div>"+
                    "</div>"
                    );
                    $("#selectorden-"+termino.pk).val(termino.fields.orden);

                });
            }
            $('select').material_select();
            $('#modalEditarActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function agregarTerminoOrdenamiento(){
    $('#actividadContenido').append(
        "<div class='row termino'>"+
            "<div class='input-field col s7'>"+
                "<textarea name='texto' class='materialize-textarea texto'></textarea>"+
                "<label for='Texto'>Texto</label>"+
            "</div>"+
            "<div class='input-field col s3'>"+
                            "<select id='selectorden' class='orden' name='orden'>"+
                                "<option value='1'>1</option>"+
                                "<option value='2'>2</option>"+
                                "<option value='3'>3</option>"+
                                "<option value='4'>4</option>"+
                                "<option value='5'>5</option>"+
                                "<option value='6'>6</option>"+
                                "<option value='7'>7</option>"+
                                "<option value='8'>8</option>"+
                                "<option value='9'>9</option>"+
                                "<option value='10'>10</option>"+
                            "</select>"+
                            "<label>Orden</label>"+
                        "</div>"+
            "<div class='row col s2'>"+
                "<a class='btn-floating btn-large waves-effect waves-light red right' onclick='eliminarTermino(this)'><i class='material-icons'>delete</i></a>"+
            "</div>"+
        "</div>"
    );
    $('select').material_select();
}

function guardarOrdenamiento(idActividad){
    var terminos = [];
    var enunciado = $("#ordenamientoEnunciado").val();
    $(".row.termino").each(function() {
        var texto = $(this).find( "textarea" ).val();
        var orden = $(this).find( "select" ).val();
        terminos.push({ 
            "texto" : texto,
            "orden"  : orden
        });
    });
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/GuardarOrdenamiento/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad,enunciado : enunciado, terminos : JSON.stringify(terminos), csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#btnVerActividad"+idActividad).removeAttr('disabled');
            Materialize.toast(data.result, 3000)
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
        }
    });
}

function crearAsociacion(){
    var oaId = $("#oaid").val();
    var nombreActividad = $("#nombreactividad").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/CrearAsociacion/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId,nombreactividad: nombreActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            var idActividad = data.asociacionId;
            $("#actividades").show();
            $("#listaactividades").append(
             "<tr id='actividad"+idActividad+"'>"+
                "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                "<td>Asociacion</td>"+
                "<td>"+
                    "<button onclick='modalEditarAsociacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                    "<button id='btnVerActividad"+idActividad+"' onclick='verAsociacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left' disabled><i class='material-icons'>visibility</i></button>"+
                    "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                "</td>"+
              "</tr>"
            );
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al crear actividad', 3000)
        }
    });
}

function modalEditarAsociacion(idActividad){
    $('#modalEditarActividadContenido').html('');
    $('#modalEditarActividadContenido').append(
        "<div class='input-field col s12'>"+
            "<textarea id='asociacionEnunciado' name='asociacionEnunciado' class='materialize-textarea'></textarea>"+
            "<label class='active' for='asociacionEnunciado'>Enunciado</label>"+
        "</div>"+
        "<div id='actividadContenido'></div>"+
        "<div class='row col s12'>"+
            "<button id='btnAgregarTermino' class='btn waves-effect waves-light red left' onclick='agregarTerminoAsociacion()'><i class='material-icons left'></i>Agregar Termino</button>"+
        "</div>"
    );
    $("#btnGuardarActividad").attr("onclick","guardarAsociacion("+idActividad+")");
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosAsociacion/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            if(data.enunciado !==''){
                $("#asociacionEnunciado").val(data.enunciado);
            }
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#actividadContenido").append(
                    "<div class='row termino'>"+
                        "<div class='input-field col s5'>"+
                            "<div class='editor campo1' id='campo1-"+termino.pk+"'>"+
                            "</div>"+
                        "</div>"+
                        "<div class='input-field col s5'>"+
                            "<div class='editor campo2' id='campo2-"+termino.pk+"'>"+
                            "</div>"+
                        "</div>"+
                        "<div class='row col s2'>"+
                            "<a class='btn-floating btn-large waves-effect waves-light red right' onclick='eliminarTermino(this)'><i class='material-icons'>delete</i></a>"+
                        "</div>"+
                    "</div>"
                    );
                    inicializarEditorPorId("campo1-"+termino.pk);
                    inicializarEditorPorId("campo2-"+termino.pk);
                    $("#campo1-"+termino.pk).code(termino.fields.campo1);
                    $("#campo2-"+termino.pk).code(termino.fields.campo2);
                });
            }
            $('#modalEditarActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function agregarTerminoAsociacion(){
    $('#actividadContenido').append(
        "<div class='row termino'>"+
            "<div class='input-field col s5'>"+
                "<div class='editor campo1'>"+
                "</div>"+
            "</div>"+
            "<div class='input-field col s5'>"+
                "<div class='editor campo2'>"+
                "</div>"+
            "</div>"+
            "<div class='row col s2'>"+
                "<a class='btn-floating btn-large waves-effect waves-light red right' onclick='eliminarTermino(this)'><i class='material-icons'>delete</i></a>"+
            "</div>"+
        "</div>"
    );
    
    inicializarEditorPorClase(".editor.campo1");
    inicializarEditorPorClase(".editor.campo2");
}

function guardarAsociacion(idActividad){
    var terminos = [];
    var enunciado = $("#asociacionEnunciado").val();
    $(".row.termino").each(function() {
        var campo1 = $(this).find( ".editor.campo1" ).code();
        var campo2 = $(this).find( ".editor.campo2" ).code();
        terminos.push({ 
            "campo1" : campo1,
            "campo2"  : campo2
        });
    });
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/GuardarAsociacion/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad,enunciado : enunciado, terminos : JSON.stringify(terminos), csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#btnVerActividad"+idActividad).removeAttr('disabled');
            Materialize.toast(data.result, 3000)
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
        }
    });
}

function crearVideo(){
    var oaId = $("#oaid").val();
    var nombreActividad = $("#nombreactividad").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        //url : "CrearVideo/", // the endpoint
        url : "/CrearOA/CrearVideo/",
        type : "POST", // http method
        data : { oaid : oaId,nombreactividad: nombreActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            var idActividad = data.videoId;
            $("#actividades").show();
            $("#listaactividades").append(
             "<tr id='actividad"+idActividad+"'>"+
                "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                "<td>Video</td>"+
                "<td>"+
                    "<button onclick='modalEditarVideo("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                    "<button id='btnVerActividad"+idActividad+"' onclick='verVideo("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left' disabled><i class='material-icons'>visibility</i></button>"+
                    "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                "</td>"+
              "</tr>"
            );
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al crear actividad', 3000)
        }
    });
}

function modalEditarVideo(idActividad){
    $('#modalEditarActividadContenido').html('');
    $('#modalEditarActividadContenido').append(
        "<div class='input-field col s12'>"+
            "<textarea id='videoDescripcion' name='videoDescripcion' class='materialize-textarea'></textarea>"+
            "<label class='active' for='videoDescripcion'>Descripcion</label>"+
        "</div>"+
        "<div class='input-field col s7'>"+
          "<input id='videoUrl' class='videoUrl' type='text'>"+
          "<label for='videoUrl' class=''>Url</label>"+
        "</div>"
    );
    $("#btnGuardarActividad").attr("onclick","guardarVideo("+idActividad+")");
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosVideo/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            if(data.descripcion !==''){
                $("#videoDescripcion").val(data.descripcion);
            }
            if(data.link !==''){
                $("#videoUrl").val(data.link);
            }
            $('#modalEditarActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function guardarVideo(idActividad){
    var terminos = [];
    var descripcion = $("#videoDescripcion").val();
    var link = $("#videoUrl").val();

    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/GuardarVideo/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad,descripcion : descripcion, link : link, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#btnVerActividad"+idActividad).removeAttr('disabled');
            Materialize.toast(data.result, 3000)
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
        }
    });
}

function eliminarActividad(idActividad){

    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/EliminarActividad/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#actividad"+idActividad).remove();
            Materialize.toast(data.result, 3000)
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
        }
    });
}

