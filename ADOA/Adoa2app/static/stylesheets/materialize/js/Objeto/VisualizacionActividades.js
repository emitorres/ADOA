$(document).ready(function() {
    $('select').material_select();
  });
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
			$divVideoPadre = $("<div class='offset-s2 col s8'>");
			$divVideoHijo = $("<div class='video-container'>");
            $divVideoHijo.append(embeberVideo(data.link));
			$divVideoPadre.append($divVideoHijo);
			$divVideoDescripcion = $("<div class='col s12'>").append("<p><b>"+data.descripcion+"</b></p>");

			$('#modalVerActividadContenido')
			.append($divVideoPadre)
			.append($divVideoDescripcion);
			
			
			
			/*
            $('#modalVerActividadContenido').append(
            "<div class='offset-s2 col s8'>"+
                "<div class='video-container'>"+
                    "<iframe  src='"+data.link+"' frameborder='0' allowfullscreen></iframe>"+
                "</div>"+
            "</div>"+
            "<div class='col s12'>"+
                "<p><b>"+data.descripcion+"</b></p>"+
            "</div>"
            );*/
            
            $('#modalVerActividad').openModal();
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al cargar las secciones', 3000)
        }
    });
}

function embeberVideo(url){
// video url patterns(youtube, instagram, vimeo, dailymotion, youku, mp4, ogg, webm)
      var ytRegExp = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
      var ytMatch = url.match(ytRegExp);

      var igRegExp = /(?:www\.|\/\/)instagram\.com\/p\/(.[a-zA-Z0-9_-]*)/;
      var igMatch = url.match(igRegExp);

      var vRegExp = /\/\/vine\.co\/v\/([a-zA-Z0-9]+)/;
      var vMatch = url.match(vRegExp);

      var vimRegExp = /\/\/(player\.)?vimeo\.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*/;
      var vimMatch = url.match(vimRegExp);

      var dmRegExp = /.+dailymotion.com\/(video|hub)\/([^_]+)[^#]*(#video=([^_&]+))?/;
      var dmMatch = url.match(dmRegExp);

      var youkuRegExp = /\/\/v\.youku\.com\/v_show\/id_(\w+)=*\.html/;
      var youkuMatch = url.match(youkuRegExp);

      var mp4RegExp = /^.+.(mp4|m4v)$/;
      var mp4Match = url.match(mp4RegExp);

      var oggRegExp = /^.+.(ogg|ogv)$/;
      var oggMatch = url.match(oggRegExp);

      var webmRegExp = /^.+.(webm)$/;
      var webmMatch = url.match(webmRegExp);

      var $video;
      if (ytMatch && ytMatch[1].length === 11) {
        var youtubeId = ytMatch[1];
        $video = $('<iframe allowfullscreen>')
            .attr('frameborder', 0)
            .attr('src', '//www.youtube.com/embed/' + youtubeId)
            .attr('width', '640').attr('height', '360');
      } else if (igMatch && igMatch[0].length) {
        $video = $('<iframe allowfullscreen>')
            .attr('frameborder', 0)
            .attr('src', 'https://instagram.com/p/' + igMatch[1] + '/embed/')
            .attr('width', '612').attr('height', '710')
            .attr('scrolling', 'yes')
            .attr('allowtransparency', 'true');
      } else if (vMatch && vMatch[0].length) {
        $video = $('<iframe allowfullscreen>')
            .attr('frameborder', 0)
            .attr('src', vMatch[0] + '/embed/simple')
            .attr('width', '600').attr('height', '600')
            .attr('class', 'vine-embed');
      } else if (vimMatch && vimMatch[3].length) {
        $video = $('<iframe webkitallowfullscreen mozallowfullscreen allowfullscreen>')
            .attr('frameborder', 0)
            .attr('src', '//player.vimeo.com/video/' + vimMatch[3])
            .attr('width', '640').attr('height', '360');
      } else if (dmMatch && dmMatch[2].length) {
        $video = $('<iframe>')
            .attr('frameborder', 0)
            .attr('src', '//www.dailymotion.com/embed/video/' + dmMatch[2])
            .attr('width', '640').attr('height', '360');
      } else if (youkuMatch && youkuMatch[1].length) {
        $video = $('<iframe webkitallowfullscreen mozallowfullscreen allowfullscreen>')
            .attr('frameborder', 0)
            .attr('height', '498')
            .attr('width', '510')
            .attr('src', '//player.youku.com/embed/' + youkuMatch[1]);
      } else if (mp4Match || oggMatch || webmMatch) {
        $video = $('<video controls>')
            .attr('src', url)
            .attr('width', '640').attr('height', '360');
      } else {
        // this is not a known video link. Now what, Cat? Now what?
		$video = $("<iframe allowfullscreen>");
		$video.attr('src', url);
      }

      return $video[0];
}
	
