function agregarPreguntaEvaluacion(){
    $('#modalEditarPreguntaContenido').html('');
    $('#modalEditarPreguntaContenido').append(
    "<div class='input-field col s12'>"+
        "<input name='pregunta' type='text' class='validate'>"+
        "<label for='pregunta' class=''>Pregunta</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input name='respuestacorrecta' type='text' class='validate'>"+
        "<label for='respuestacorrecta' class=''>Respuesta Correcta</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input name='respuestaincorrecta1' type='text' class='validate'>"+
        "<label for='respuestaincorrecta1' class=''>Respuesta Incorrecta 1</label>"+
    "</div>"+
    "<div class='input-field col s12'>"+
        "<input name='respuestaincorrecta2' type='text' class='validate'>"+
        "<label for='respuestaincorrecta2' class=''>Respuesta Incorrecta 2</label>"+
    "</div>");
    $('#modalEditarPregunta').openModal();
}