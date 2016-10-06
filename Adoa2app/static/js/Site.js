// Initialize collapse button
$(".dropdown-button").dropdown();
$(".button-collapse").sideNav();
$('select').material_select();
$('.modal-trigger').leanModal();
$('.slider').slider({full_width: true});
cargarListaPatrones()

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

        $('.editor').materialnote({
            toolbar: toolbar,
            height: 100,
            minHeight: 100,
            defaultBackColor: '#fff'
        });

function cambiarTab(tabContentId,tabId){
    $("#"+tabId).removeClass("disabled");
    $('ul.tabs').tabs('select_tab', tabContentId);
}

function cerrarModal(id){
    $('#'+id).closeModal();
}

$('#oa-paso1').on('submit', function(event){
    event.preventDefault();
    var oaTitulo = $("#oatitulo").val();
    var oaDescripcion = $("#oadescripcion").val();
    var oaPatron = $("#oapatron").val();
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "paso1/", // the endpoint
        type : "POST", // http method
        data : { titulo : oaTitulo, descripcion : oaDescripcion, patron : oaPatron, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#oaid").val(data.oaid);
            Materialize.toast('Informacion guardada con exito!!', 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar la Informacion', 3000, 'rounded')
        }
    });
});

$('#oa-paso2').on('submit', function(event){
    event.preventDefault();
    var oaIntroduccion = $("#introduccion-oa").code();
    var oaId = $("#oaid").val();
    var csrf = $( "#oa-paso2" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "paso2/", // the endpoint
        type : "POST", // http method
        data : { oaid : oaId, introduccion : oaIntroduccion, csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            $("#oaid").val(data.oaid);
            Materialize.toast('Introduccion guardada con exito!!', 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar la Introduccion', 3000, 'rounded')
        }
    });
});

function cargarListaPatrones(){
    var csrf = $( "#oa-paso1" ).children('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url : "traerPatrones/", // the endpoint
        type : "POST", // http method
        data : { csrfmiddlewaretoken: csrf }, // data sent with the post request
        success : function(data) {
            data.forEach(function(patron) {
                $("#oapatron").append("<option value='"+patron.pk+"'>"+patron.fields.nombre+"</option>");
            })
            $("#oapatron").material_select();
            Materialize.toast('Patrones cargados con exito!!', 3000, 'rounded')
        },
        error : function(xhr,errmsg,err) {
            Materialize.toast('Error al guardar la Informacion', 3000, 'rounded')
        }
    });
}



