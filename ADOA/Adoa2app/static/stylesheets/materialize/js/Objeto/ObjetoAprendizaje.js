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
if($("#oaid").length){
    cargarListaPatrones();
    cargarDatosGuardados();
}
if($("#tablaObjetos").length){
        cargarTablaObjetos();
    }

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
            cambiarTab('contentTab2','tab2');
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
            cambiarTab('contentTab3','tab3');
            $("#btnGuardarPaso2").removeClass('red');
            $("#btnGuardarPaso2").addClass('green');
            $("#btnGuardarPaso2").html('Editar');
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
            cambiarTab('contentTab4','tab4');   
            $("#btnGuardarPaso3").removeClass('red');
            $("#btnGuardarPaso3").addClass('green');
            $("#btnGuardarPaso3").html('Editar');
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
    
    if($("#editoa").val() !== ""){
        $("#tituloAccion").html("Editar Objeto");
        var oaId = $("#editoa").val();
        var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url : "/CrearOA/TraerDatosObjeto/", // the endpoint
            type : "POST", // http method
            data : { oaid : oaId, csrfmiddlewaretoken: csrf }, // data sent with the post request
            success : function(data) {
                var objeto = JSON.parse(data.objeto);
                var patron = JSON.parse(data.patron);
                var evaluacion = JSON.parse(data.evaluacion);
                var evaluacionItems = JSON.parse(data.evaluacionItems);
                var verdaderofalsolista = JSON.parse(data.verdaderofalso);
                var ordenamientolista = JSON.parse(data.ordenamiento);
                var videolista = JSON.parse(data.video);
                var identificacionlista = JSON.parse(data.identificacion);
                var asociacionlista = JSON.parse(data.asociacion);
                var seccionesNombre = JSON.parse(data.seccionesNombre);
                var seccionesContenido = JSON.parse(data.seccionesContenido);
            
                $("#oaid").val(objeto[0].pk);
                $("#evaluacionid").val(evaluacion[0].pk);
                $("#oatitulo").val(objeto[0].fields.titulo);
                $("#labeltitulo").addClass("active");
                $("#oadescripcion").val(objeto[0].fields.descripcion);
                $("#labeldescripcion").addClass("active");
    
                $("#introduccion-oa").code(objeto[0].fields.introduccion);
                
                $("#oapatron").val(patron[0].pk);
                $("#oapatron").material_select();
                
                
                seccionesNombre.forEach(function(seccion) {
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
                
                seccionesContenido.forEach(function(seccion) {
                    $("#seccion"+seccion.fields.SeccionNombre).code(seccion.fields.contenido);
                    
                });
                
                verdaderofalsolista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<li id='actividad"+idActividad+"' class='collection-item'><div>"+nombreActividad.substr(0, 50)+" (Verdadero o Falso)"+
                    "<a onclick='eliminarActividad("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>delete</i></a>"+
                    "<a onclick='verVerdaderoFalso("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>visibility</i></a>"+
                    "<a onclick='modalEditarVerdaderoFalso("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>mode_edit</i></a>"+
                    "</div></li>"
                    );
                });
                
                ordenamientolista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<li id='actividad"+idActividad+"' class='collection-item'><div>"+nombreActividad.substr(0, 50)+" (Ordenamiento)"+
                    "<a onclick='eliminarActividad("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>delete</i></a>"+
                    "<a onclick='verOrdenamiento("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>visibility</i></a>"+
                    "<a onclick='modalEditarOrdenamiento("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>mode_edit</i></a>"+
                    "</div></li>"
                    );
                });
                
                identificacionlista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<li id='actividad"+idActividad+"' class='collection-item'><div>"+nombreActividad.substr(0, 50)+" (Identificacion)"+
                    "<a onclick='eliminarActividad("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>delete</i></a>"+
                    "<a onclick='verIdentificacion("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>visibility</i></a>"+
                    "<a onclick='modalEditarIdentificacion("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>mode_edit</i></a>"+
                    "</div></li>"
                    );
                });
                
                asociacionlista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<li id='actividad"+idActividad+"' class='collection-item'><div>"+nombreActividad.substr(0, 50)+" (Asociacion)"+
                    "<a onclick='eliminarActividad("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>delete</i></a>"+
                    "<a onclick='verAsociacion("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>visibility</i></a>"+
                    "<a onclick='modalEditarAsociacion("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>mode_edit</i></a>"+
                    "</div></li>"
                    );
                });
                
                videolista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<li id='actividad"+idActividad+"' class='collection-item'><div>"+nombreActividad.substr(0, 50)+" (Video)"+
                    "<a onclick='eliminarActividad("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>delete</i></a>"+
                    "<a onclick='verVideo("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>visibility</i></a>"+
                    "<a onclick='modalEditarVideo("+idActividad+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>mode_edit</i></a>"+
                    "</div></li>"
                    );
                });
                
                
                evaluacionItems.forEach(function(pregunta) {
                    var idPregunta = pregunta.pk;
                    var preguntatexto = pregunta.fields.pregunta;
                    $("#preguntas").show();
                    $("#listapreguntas").append(
                    "<li id='pregunta"+idPregunta+"' class='collection-item'><div>"+preguntatexto.substr(0,140)+
                    "<a onclick='eliminarPregunta("+idPregunta+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>delete</i></a>"+
                    "<a onclick='modalEditarPregunta("+idPregunta+")' href='#!' class='btn-floating waves-effect waves-light red btn-actividad right'><i class='material-icons'>mode_edit</i></a>"+
                    "</div></li>"
                    );
                    $("#btnVerEvaluacion").show();
                });
                
                
                $("#btnTab1").removeClass('disabled');
                $("#btnGuardarPaso1").removeClass('red');
                $("#btnGuardarPaso1").addClass('green');
                $("#btnGuardarPaso1").html('Editar');
                $("#btnGuardarPaso2").removeClass('red');
                $("#btnGuardarPaso2").addClass('green');
                $("#btnGuardarPaso2").html('Editar');
                $("#btnGuardarPaso3").removeClass('red');
                $("#btnGuardarPaso3").addClass('green');
                $("#btnGuardarPaso3").html('Editar');
                $(".tab").removeClass("disabled");
                
                Materialize.toast("Objeto cargado con exito", 3000, 'rounded')
            },
            error : function(xhr,errmsg,err) {
                Materialize.toast('Error al cargar el objeto', 3000, 'rounded')
            }
        });
    }
    
}

function cargarTablaObjetos(){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url : "TraerObjetos/", // the endpoint
            type : "POST", // http method
            data : { csrfmiddlewaretoken: csrf }, // data sent with the post request
            success : function(data) {
                data.forEach(function(objeto) {
                    $("#bodyTablaObjetos").append(
                    "<tr>"+
                        "<td>"+objeto.pk+"</td>"+
                        "<td>"+objeto.fields.titulo.substring(0, 20)+"</td>"+
                        "<td>"+objeto.fields.descripcion.substring(0, 40)+"</td>"+
                        "<td>"+
                        "<a href='!#' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>play_for_work</i></a>"+
                        "<a href='/EditarOA/"+objeto.pk+"' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>mode_edit</i></a>"+
                        "<a href='!#' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>delete</i></a>"+
                        "</td>"+
                    "</tr>"
                    );
                });
                $('#tablaObjetos').DataTable();
            },
            error : function(xhr,errmsg,err) {
                Materialize.toast('Error al cargar los patrones pedagogicos', 3000, 'rounded')
            }
        });
    }
