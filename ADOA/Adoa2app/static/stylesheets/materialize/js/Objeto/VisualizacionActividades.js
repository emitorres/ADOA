function verVerdaderoFalso(idActividad){
    $('#modalVerActividadContenido').html('');
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosVerdaderoFalso/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $('#modalVerActividadContenido').append(
            "<div class='col s12'>"+
                "<p><b>"+data.enunciado+"</b></p>"+
            "</div>"
            );
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#modalVerActividadContenido").append(
                    "<div class='row'>"+
                        "<div class='col s6'>"+
                            "<p>"+termino.fields.afirmacion+"</p>"+
                        "</div>"+
                        "<div class='input-field col s3'>"+
                            "<select id='selectVerdaderoFalso"+termino.pk+"' class='selectVerdaderoFalso' name='selectVerdaderoFalso'>"+
                                "<option value='' disabled='' selected=''>Seleccione la respuesta</option>"+
                                "<option value='0' >Falso</option>"+
                                "<option value='1' >Verdadero</option>"+
                            "</select>"+
                            "<label>Respuesta</label>"+
                        "</div>"+
                        "<input type='hidden' class='respuestaVerdaderoFalso' name='respuesta"+termino.pk+"' data-id='"+termino.pk+"' id='respuesta"+termino.pk+"' value=''>"+
                        "<div class='col s3' id='resultado"+termino.pk+"'>"+
                        "</div>"+
                    "</div>"
                    );
                    if(termino.fields.respuesta === true){
                        $("#respuesta"+termino.pk).val('1');
                    }else{
                        $("#respuesta"+termino.pk).val('0');
                    }
                    
                });
                $("#modalVerActividadContenido").append(
                    "<div class='row col s12'>"+
                        "<a class='btn waves-effect waves-light right red' onclick='validarRespuestasVerdaderoFalso()'>Correccion</a>"+
                    "</div>"
                );
            }
            $('select').material_select();
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function validarRespuestasVerdaderoFalso(){
    $(".respuestaVerdaderoFalso").each(function() {
        var id = $(this).data("id");
        if($("#selectVerdaderoFalso"+id).val() == $("#respuesta"+id).val()){
            $("#resultado"+id).html("<div class='chip chip-actividad green'> CORRECTO </div>");
        }else{
            $("#resultado"+id).html("<div class='chip chip-actividad red'> INCORRECTO </div>");
        }
    });
}

function verIdentificacion(idActividad){
    $('#modalVerActividadContenido').html('');
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosIdentificacion/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $('#modalVerActividadContenido').append(
            "<div class='col s12'>"+
                "<p><b>"+data.enunciado+"</b></p>"+
            "</div>"
            );
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#modalVerActividadContenido").append(
                    "<div class='row'>"+
                        "<div class='col s6'>"+
                            "<p>"+termino.fields.concepto+"</p>"+
                        "</div>"+
                        "<div class='input-field col s3'>"+
                            "<select id='selectIdentificacion"+termino.pk+"' class='selectIdentificacion' name='selectIdentificacion'>"+
                                "<option value='' disabled='' selected=''>Seleccione si corresponde</option>"+
                                "<option value='0' >No</option>"+
                                "<option value='1' >Si</option>"+
                            "</select>"+
                            "<label>Corresponde</label>"+
                        "</div>"+
                        "<input type='hidden' class='respuestaIdentificacion' name='respuesta"+termino.pk+"' data-id='"+termino.pk+"' id='respuesta"+termino.pk+"' value=''>"+
                        "<div class='col s3' id='resultado"+termino.pk+"'>"+
                        "</div>"+
                    "</div>"
                    );
                    if(termino.fields.respuesta === true){
                        $("#respuesta"+termino.pk).val('1');
                    }else{
                        $("#respuesta"+termino.pk).val('0');
                    }
                    
                });
                $("#modalVerActividadContenido").append(
                    "<div class='row col s12'>"+
                        "<a class='btn waves-effect waves-light right red' onclick='validarRespuestasIdentificacion()'>Correccion</a>"+
                    "</div>"
                );
            }
            $('select').material_select();
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function validarRespuestasIdentificacion(){
    $(".respuestaIdentificacion").each(function() {
        var id = $(this).data("id");
        if($("#selectIdentificacion"+id).val() == $("#respuesta"+id).val()){
            $("#resultado"+id).html("<div class='chip chip-actividad green'> CORRECTO </div>");
        }else{
            $("#resultado"+id).html("<div class='chip chip-actividad red'> INCORRECTO </div>");
        }
    });
}

function verAsociacion(idActividad){
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosAsociacion/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function verOrdenamiento(idActividad){
    $('#modalVerActividadContenido').html('');
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosOrdenamiento/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $('#modalVerActividadContenido').append(
            "<div class='col s12'>"+
                "<p><b>"+data.enunciado+"</b></p>"+
            "</div>"
            );
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#modalVerActividadContenido").append(
                    "<div class='row'>"+
                        "<div class='col s6'>"+
                            "<p>"+termino.fields.texto+"</p>"+
                        "</div>"+
                        "<div class='input-field col s3'>"+
                            "<select id='selectOrdenamiento"+termino.pk+"' class='selectOrdenamiento' name='selectOrdenamiento'>"+
                                "<option value='' disabled='' selected=''>Seleccione el orden</option>"+
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
                        "<input type='hidden' class='respuestaOrdenamiento' name='respuesta"+termino.pk+"' data-id='"+termino.pk+"' id='respuesta"+termino.pk+"' value=''>"+
                        "<div class='col s3' id='resultado"+termino.pk+"'>"+
                        "</div>"+
                    "</div>"
                    );
                    $("#respuesta"+termino.pk).val(termino.fields.orden);
                });
                $("#modalVerActividadContenido").append(
                    "<div class='row col s12'>"+
                        "<a class='btn waves-effect waves-light right red' onclick='validarRespuestasOrdenamiento()'>Correccion</a>"+
                    "</div>"
                );
            }
            $('select').material_select();
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function validarRespuestasOrdenamiento(){
    $(".respuestaOrdenamiento").each(function() {
        var id = $(this).data("id");
        if($("#selectOrdenamiento"+id).val() == $("#respuesta"+id).val()){
            $("#resultado"+id).html("<div class='chip chip-actividad green'> CORRECTO </div>");
        }else{
            $("#resultado"+id).html("<div class='chip chip-actividad red'> INCORRECTO </div>");
        }
    });
}

function verVideo(idActividad){
       $('#modalVerActividadContenido').html('');
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosVideo/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $('#modalVerActividadContenido').append(
            "<div class='offset-s2 col s8'>"+
                "<div class='video-container'>"+
                    "<iframe  src='"+data.link+"' frameborder='0' allowfullscreen></iframe>"+
                "</div>"+
            "</div>"+
            "<div class='col s12'>"+
                "<p><b>"+data.descripcion+"</b></p>"+
            "</div>"
            );
            
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}
