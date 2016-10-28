function verEvaluacion(){

    var evaluacionId = $("#evaluacionid").val();
    $('#modalVerEvaluacionContenido').html('');
    
    var csrf = $( "#oa-paso3" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerTerminosEvaluacion/", // the endpoint
        type : "POST", // http method
        data : { evaluacionid : evaluacionId, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $('#modalVerEvaluacionContenido').append(
            "<div class='col s12'>"+
                "<p><b>"+data.enunciado+"</b></p>"+
            "</div>"
            );
            if(data.terminos != '[]'){
                var terminos = JSON.parse(data.terminos);
                terminos.forEach(function(termino) {
                    $("#modalVerEvaluacionContenido").append(
                    "<div class='row'>"+
                            "<div class='col s9'>"+
                                "<b>"+termino.fields.pregunta+"</b>"+
                            "</div>"+
                            "<div class='col s3' id='resultado"+termino.pk+"'>"+
                            "</div>"+
                            "<div class='col s12 hoverable'>"+
                                "<div class='col s9'>"+
                                    "<p id='respuesta1-"+termino.pk+"'></p>"+
                                "</div>"+
                                "<div class='col s3'>"+
                                    "<p>"+
                                        "<input name='group1"+termino.pk+"' type='radio' data-id='"+termino.pk+"' id='radiorespuesta1-"+termino.pk+"' />"+
                                        "<label for='radiorespuesta1-"+termino.pk+"'></label>"+
                                    "</p>"+
                                "</div>"+
                            "</div>"+
                            "<div class='col s12 hoverable'>"+
                                "<div class='col s9'>"+
                                    "<p id='respuesta2-"+termino.pk+"'></p>"+
                                "</div>"+
                                "<div class='col s3'>"+
                                    "<p>"+
                                        "<input name='group1"+termino.pk+"' type='radio' data-id='"+termino.pk+"' id='radiorespuesta2-"+termino.pk+"' />"+
                                        "<label for='radiorespuesta2-"+termino.pk+"'></label>"+
                                    "</p>"+
                                "</div>"+
                            "</div>"+
                            "<div class='col s12 hoverable'>"+
                                "<div class='col s9'>"+
                                    "<p id='respuesta3-"+termino.pk+"'></p>"+
                                "</div>"+
                                "<div class='col s3'>"+
                                    "<p >"+
                                        "<input name='group1"+termino.pk+"' type='radio' data-id='"+termino.pk+"' id='radiorespuesta3-"+termino.pk+"' />"+
                                        "<label for='radiorespuesta3-"+termino.pk+"'></label>"+
                                    "</p>"+
                                "</div>"+
                            "</div>"+
                    "</div>"
                    );
                    
                    $("#radiorespuesta"+termino.fields.ordenRespuestaCorrecta+"-"+termino.pk).addClass("correcta");
                    $("#respuesta"+termino.fields.ordenRespuestaCorrecta+"-"+termino.pk).html(termino.fields.respuestaCorrecta);
                    $("#respuesta"+termino.fields.ordenRespuestaIncorrecta1+"-"+termino.pk).html(termino.fields.respuestaIncorrecta1);
                    $("#respuesta"+termino.fields.ordenRespuestaIncorrecta2+"-"+termino.pk).html(termino.fields.respuestaIncorrecta2);
                    $("#modalVerEvaluacionContenido").append(
                    "<div class='divider'></div>"
                    );
                    
                });
                $("#modalVerEvaluacionContenido").append(
                    "<div class='row col s12'>"+
                        "<a class='btn waves-effect waves-light right red' onclick='validarRespuestasEvaluacion()'>Correccion</a>"+
                    "</div>"
                );
            }
            
            $('#modalVerEvaluacion').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000, 'rounded')
        }
    });
}

function validarRespuestasEvaluacion(){
    $(".correcta").each(function() {
        var id = $(this).data("id");
        if($(this).is(':checked')){
            $("#resultado"+id).html("<div class='chip chip-actividad green'> CORRECTO </div>");
        }else{
            $("#resultado"+id).html("<div class='chip chip-actividad red'> INCORRECTO </div>");
        }
    });
}