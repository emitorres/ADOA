function verVerdaderoFalso(idActividad){
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "VerVerdaderoFalso/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            if(data.enunciado !==''){
                $("#verdaderoFalsoEnunciado").val(data.enunciado);
            }
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#modalVerActividadContenido").append(
                    "<div class='row'>"+
                        "<div class='col s7'>"+
                            "<label>"+termino.fields.afirmacion+"</label>"+
                        "</div>"+
                        "<div class='input-field col s3'>"+
                            "<select actividadId='"+termino.pk+"' class='selectVerdaderoFalso' name='selectVerdaderoFalso'>"+
                                "<option value='' disabled='' selected=''>Seleccione la respuesta</option>"+
                                "<option value='0' >Falso</option>"+
                                "<option value='1' >Verdadero</option>"+
                            "</select>"+
                            "<label>Respuesta</label>"+
                        "</div>"+
                        "<input type='hidden' name='respuesta"+termino.pk+"' id='respuesta"+termino.pk+"' value=''>"+
                    "</div>"
                    );
                    if(termino.fields.respuesta === true){
                        $("#respuesta-"+termino.pk).val('1');
                    }else{
                        $("#respuesta-"+termino.pk).val('0');
                    }
                    
                });
                $("#modalVerActividadContenido").append();
            }
            $('select').material_select();
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}

function validarRespuestaVerdaderoFalso(this){
    
}

function verIdentificacion(idActividad){
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "VerIdentificacion/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}

function verAsociacion(idActividad){
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "VerAsociacion/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}

function verOrdenamiento(idActividad){
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "VerOrdenamiento/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}

function verVideo(idActividad){
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "VerVideo/", // the endpoint
        type : "POST", // http method
        data : { actividadId : idActividad, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}