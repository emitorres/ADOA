var evaluacionPrevisualizada = false;

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
    var tipo = parseInt($("#tablaObjetos").attr("name"));
    switch (tipo){
        case 1:
            cargarMisObjetos();
            break;
        case 2:
            cargarTodosLosObjetos();
            break;
    
    }
}

if($("#contenidoTarjeta").length){
    var tipo = parseInt($("#contenidoTarjeta").attr("name"));
    switch (tipo){
        
        case 1:
            cargarObjetosSinTerminar();
            break;
    }
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
            
            Materialize.toast(data.result, 3000);
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
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
            Materialize.toast('Guardado con exito!!', 3000)
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
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
            Materialize.toast(data.result, 3000)
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar el objeto', 3000);
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
            Materialize.toast('Error al cargar los patrones pedagogicos', 3000);
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
            Materialize.toast('Error al cargar las secciones', 3000);
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
                    "<tr id='actividad"+idActividad+"'>"+
                        "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                        "<td>Verdadero o Falso</td>"+
                        "<td>"+
                            "<button onclick='modalEditarVerdaderoFalso("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                            "<button id='btnVerActividad"+idActividad+"' onclick='verVerdaderoFalso("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                            "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                        "</td>"+
                    "</tr>"
                    );
                    
                });
                
                ordenamientolista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<tr id='actividad"+idActividad+"'>"+
                        "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                        "<td>Ordenamiento</td>"+
                        "<td>"+
                            "<button onclick='modalEditarOrdenamiento("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                            "<button id='verOrdenamiento"+idActividad+"' onclick='verOrdenamiento("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                            "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                        "</td>"+
                    "</tr>"
                    );
                });
                
                identificacionlista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<tr id='actividad"+idActividad+"'>"+
                        "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                        "<td>Identificacion</td>"+
                        "<td>"+
                            "<button onclick='modalEditarIdentificacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                            "<button id='btnVerActividad"+idActividad+"' onclick='verIdentificacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                            "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                        "</td>"+
                    "</tr>"
                    );
                });
                
                asociacionlista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<tr id='actividad"+idActividad+"'>"+
                        "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                        "<td>Asociacion</td>"+
                        "<td>"+
                            "<button onclick='modalEditarAsociacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                            "<button id='btnVerActividad"+idActividad+"' onclick='verAsociacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                            "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                        "</td>"+
                    "</tr>"
                    );
                });
                
                videolista.forEach(function(actividad) {
                    $("#actividades").show();
                    var idActividad = actividad.pk;
                    var nombreActividad = actividad.fields.nombre;
                    $("#listaactividades").append(
                    "<tr id='actividad"+idActividad+"'>"+
                        "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                        "<td>Video</td>"+
                        "<td>"+
                            "<button onclick='modalEditarVideo("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                            "<button id='btnVerActividad"+idActividad+"' onclick='verVideo("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                            "<button onclick='eliminarActividad("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                        "</td>"+
                    "</tr>"
                    );
                });
                
                
                evaluacionItems.forEach(function(pregunta) {
                    var idPregunta = pregunta.pk;
                    var preguntatexto = pregunta.fields.pregunta;
                    $("#preguntas").show();
                    $("#listapreguntas").append(
                    "<tr id='pregunta"+idPregunta+"'>"+
                        "<td>"+preguntatexto.substr(0, 140)+"</td>"+
                        "<td>"+
                            "<button onclick='modalEditarPregunta("+idPregunta+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>mode_edit</i></button>"+
                            "<button onclick='eliminarPregunta("+idPregunta+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>delete</i></button>"+
                        "</td>"+
                    "</tr>"
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
                
                Materialize.toast("Objeto cargado con exito", 3000);
            },
            error : function(xhr,errmsg,err) {
                Materialize.toast('Error al cargar el objeto', 3000);
            }
        });
    }
    
}

function cargarMisObjetos(){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url : "/Objetos/TraerMisObjetos/", // the endpoint
            type : "POST", // http method
            data : { csrfmiddlewaretoken: csrf }, // data sent with the post request
            success : function(data) {
                data.forEach(function(objeto) {
                    $("#bodyTablaObjetos").append(
                    "<tr id='miObjeto_" + objeto.pk +"'>"+
                        "<td>"+objeto.pk+"</td>"+
                        "<td>"+objeto.fields.titulo.substring(0, 20)+"</td>"+
                        "<td>"+objeto.fields.descripcion.substring(0, 40)+"</td>"+
                        "<td>"+
                        "<a href='#' onclick='previsualizarOA(" +objeto.pk+ ");' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>visibility</i></a>"+
                        "<a href='#' onclick='comprobarOA(" + objeto.pk +");' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>play_for_work</i></a>"+
                        "<a href='/EditarOA/"+objeto.pk+"' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>mode_edit</i></a>"+
                        "<a href='#' onclick='borrarOA(" +objeto.pk+ ");' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>delete</i></a>"+
                        "</td>"+
                    "</tr>"
                    );
                });
                $('#tablaObjetos').DataTable();
            },
            error : function(xhr,errmsg,err) {
                Materialize.toast('Error al cargar los patrones pedagogicos', 3000);
            }
        });
    }
    
function cargarTodosLosObjetos(){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url : "/Objetos/TraerObjetos/", // the endpoint
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
                        "<a href='#' onclick='previsualizarOA(" +objeto.pk+ ");' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>visibility</i></a>"+
                        "<a href='#' onclick='importarOA(" + objeto.pk +");' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>input</i></a>"+
                        "<a href='#' onclick='borrarOA(" +objeto.pk+ ");' class='btn-floating waves-effect waves-light red btn-actividad' ><i class='material-icons'>play_for_work</i></a>"+
                        "</td>"+
                    "</tr>"
                    );
                });
                $('#tablaObjetos').DataTable();
            },
            error : function(xhr,errmsg,err) {
                Materialize.toast('Error al cargar los patrones pedagogicos', 3000);
            }
        });
    }    
function cargarObjetosSinTerminar(){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url : "/Inicio/mostrarObjetosSinTerminar/", // the endpoint
            type : "POST", // http method
            data : { csrfmiddlewaretoken: csrf }, // data sent with the post request
            success : function(data) {
            var objetos = JSON.parse(data.objetos);
            var patrones = JSON.parse(data.patrones);
            var i = 0;
            objetos.forEach(function(objeto) {
                    $("#contenidoTarjeta").append(
                    "<div class='col s12 m6 l3'>"+
                        "<div class='card'>"+
                            "<div class='card-image waves-effect waves-block waves-light'>"+
                                "<img class='activator' src='/static/images/AdoaCard.png'>"+
                        "</div>"+
                        "<div class='card-content'>"+
                            "<span class='card-title activator grey-text text-darken-4'>"+objeto.fields.titulo.substring(0,15)+"<i class='material-icons right'>more_vert</i></span>"+
                              "<p>"+'Patron Utilizado: '+patrones[i].fields.nombre +"</p>"+

                        "</div>"+
                        "<div class='card-reveal'>"+
                            "<span class='card-title grey-text text-darken-4'>Opciones<i class='material-icons right' style='margin-bottom:50px'>close</i></span>"+
                            "<div class='row'>"+ 
                                "<a href='#' onclick='comprobarOA(" + objeto.pk +");' class=' col s12 m12 l12 btn waves-effect waves-light'style='margin-bottom:10px' >Ver Estado</a>"+
                               "<a href='/EditarOA/"+objeto.pk+"' class=' col s12 m12 l12 btn waves-effect waves-light' style='margin-bottom:10px'>Seguir Editando</a>"+
                                "<a href='#' onclick='borrarOA(" +objeto.pk+ ");'  class=' col s12 m12 l12 btn waves-effect waves-light'style='margin-bottom:10px'>Eliminar</a>"+
                            "</div>"+
                        "</div>"+
                    "</div>"
                    );
                    i++;
                });
            },
            error : function(xhr,errmsg,err) {
                Materialize.toast('Error al cargar los patrones pedagogicos', 3000);
            }
        });
    } 
function comprobarOA(id){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url : "/ComprobarOA/" + id + "/", // the endpoint
            type : "POST", // http method
            data : { csrfmiddlewaretoken: csrf }, // data sent with the post request
            success : function(json_string) {
                var data = JSON.parse( json_string );
                if (!data.Exportable){
                    var $estadoItems = $('<ul class="collection">');
                    for (var atributo in data.attrOA){
                        var $item = $('<li class="collection-item">').append(atributo);
                        var $spanItem = $('<span>')
                                    .attr('class', 'badge green')
                                    .attr('data-badge-caption', 'Completo');
                        if (data.attrOA[atributo] === false){
                            $spanItem = $('<span>')
                                        .attr('class', 'badge red')
                                        .attr('data-badge-caption', 'Incompleto');
                        }
                        
                        $item.append($spanItem);    
                        $estadoItems.append($item);       
                    }
                 
                    var $modalEstadoOAContenido = $('#modalEstadoOAContenido').html(''); 
                    var $titulo = $('<div class="row">')
                                .append('<p class="center"><b>No se puede exportar el OA si no están todas las secciones completas</b></p>');
                    var $estado =$('<div class="row">')
                                .append($estadoItems);
                    $modalEstadoOAContenido
                        .append($titulo)
                        .append($estado);
                    
                    $('#modalEstadoOA').openModal({dismissible:false});
                }else{
                    exportarOA(id);
                }
            }
        });
   }

function previsualizarOA(oaId){
    cambiarTab('informacionTab', 'tab1');
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "/CrearOA/TraerDatosObjeto/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId, csrfmiddlewaretoken: csrf },
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
            var usuario = JSON.parse(data.usuario);
            
            $("#evaluacionid").val(evaluacion[0].pk);
            $("#listaactividades").html('');
            $("#listapreguntas").html('');
            $("#oaSecciones").html('');
            $('#oaTitulo').text(objeto[0].fields.titulo);
            $('#oaDescripcion').text(objeto[0].fields.descripcion);
            $('#oaPatron').text(patron[0].fields.nombre);
            $('#oaAutor').text(usuario[0].fields.nombre + " " + usuario[0].fields.apellido);
            $('#oaIntroduccion').html(objeto[0].fields.introduccion);
                    
            seccionesNombre.forEach(function(seccion) {
                $("#oaSecciones").append("<div class='col s11 tituloSeccion'>"+seccion.fields.nombre+"</div>"+
                "<div class='row'>"+
                    "<div class='input-field col s11'>"+
                        "<div class='seccion' data-id='"+seccion.pk+"' id='seccion"+seccion.pk+"'>"+
                        "</div>"+
                    "</div>"+
                "</div>");
            });
            
            seccionesContenido.forEach(function(seccion) {
                $("#seccion"+seccion.fields.SeccionNombre).html(seccion.fields.contenido)
                .append("<div class='divider'></div>");
            });
            
            verdaderofalsolista.forEach(function(actividad) {
                $("#actividades").show();
                var idActividad = actividad.pk;
                var nombreActividad = actividad.fields.nombre;
                $("#listaactividades").append(
                "<tr id='actividad"+idActividad+"'>"+
                    "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                    "<td>Verdadero o Falso</td>"+
                    "<td>"+
                        "<button id='btnVerActividad"+idActividad+"' onclick='verVerdaderoFalso("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                    "</td>"+
                "</tr>"
                );
                
            });
            
            ordenamientolista.forEach(function(actividad) {
                $("#actividades").show();
                var idActividad = actividad.pk;
                var nombreActividad = actividad.fields.nombre;
                $("#listaactividades").append(
                "<tr id='actividad"+idActividad+"'>"+
                    "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                    "<td>Ordenamiento</td>"+
                    "<td>"+
                        "<button id='verOrdenamiento"+idActividad+"' onclick='verOrdenamiento("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                    "</td>"+
                "</tr>"
                );
            });
            
            identificacionlista.forEach(function(actividad) {
                $("#actividades").show();
                var idActividad = actividad.pk;
                var nombreActividad = actividad.fields.nombre;
                $("#listaactividades").append(
                "<tr id='actividad"+idActividad+"'>"+
                    "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                    "<td>Identificacion</td>"+
                    "<td>"+
                        "<button id='btnVerActividad"+idActividad+"' onclick='verIdentificacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                    "</td>"+
                "</tr>"
                );
            });
            
            asociacionlista.forEach(function(actividad) {
                $("#actividades").show();
                var idActividad = actividad.pk;
                var nombreActividad = actividad.fields.nombre;
                $("#listaactividades").append(
                "<tr id='actividad"+idActividad+"'>"+
                    "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                    "<td>Asociacion</td>"+
                    "<td>"+
                        "<button id='btnVerActividad"+idActividad+"' onclick='verAsociacion("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                    "</td>"+
                "</tr>"
                );
            });
            
            videolista.forEach(function(actividad) {
                $("#actividades").show();
                var idActividad = actividad.pk;
                var nombreActividad = actividad.fields.nombre;
                $("#listaactividades").append(
                "<tr id='actividad"+idActividad+"'>"+
                    "<td>"+nombreActividad.substr(0, 50)+"</td>"+
                    "<td>Video</td>"+
                    "<td>"+
                        "<button id='btnVerActividad"+idActividad+"' onclick='verVideo("+idActividad+")' class='btn-floating waves-effect waves-light red btn-actividad left'><i class='material-icons'>visibility</i></button>"+
                    "</td>"+
                "</tr>"
                );
            });
            
            verEvaluacion();
            $('#modalPrevisualizacionOA').openModal({opacity: 0.2, in_duration: 250, out_duration: 100, dismissible:false});
        }   
    });
}

function verPrevisualizacionEvaluacion(){
        if (!evaluacionPrevisualizada){
            $("#preguntasEvaluacion").html('');
            $("#modalVerEvaluacionContenido").children().appendTo("#preguntasEvaluacion");
            closeThisModal('#modalVerEvaluacion');
            evaluacionPrevisualizada = true;
        }
}

//Función para evitar que el modal quede con z-index bajo
function closeThisModal(modal){
    $(modal).closeModal({complete: function(){$(this).remove();}});
}

function cerrarPrevisualizacionOA(){
    evaluacionPrevisualizada = false;
    closeThisModal('#modalPrevisualizacionOA');
    closeThisModal('#modalVerEvaluacion');
}
   
function exportarOA(id){
    var exportLink = document.createElement('a');
    exportLink.href = "/ExportarOA/" + id + "/";
    document.body.appendChild(exportLink);
    exportLink.click();
}

function importarOA(id){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url : "/importarOA/" + id + "/", // the endpoint
            type : "POST", // http method
            data : { csrfmiddlewaretoken: csrf }, // data sent with the post request
            success : function(data) {
                Materialize.toast(data.result, 3000);
            }
        });
}

function borrarOA(id){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url : "/BorrarOA/" + id + "/", // the endpoint
            type : "POST", // http method
            data : { csrfmiddlewaretoken: csrf }, // data sent with the post request
            success : function(data) {
                if (data.code){
                    var objetoBorrado = "#miObjeto_" + id;
                    $(objetoBorrado).remove();
                }
                Materialize.toast(data.result, 3000);
            }
        });
}