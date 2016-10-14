// Initialize collapse button
$(document).ready(function(){
    $(".dropdown-button").dropdown();
    $(".button-collapse").sideNav();
    $('select').material_select();
    $('.modal-trigger').leanModal();
    $('.slider').slider({full_width: true});
    $('.collapsible').collapsible({
          accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
        });
    if($("#tablaObjetos").length){
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
                        "<td>"+objeto.fields.titulo+"</td>"+
                        "<td>"+objeto.fields.descripcion.substring(0, 20)+"</td>"+
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
});


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

function cerrarModal(id){
    $('#'+id).closeModal();
}

function inicializarEditorPorId(id){
    var toolbar = [
            ['style', ['clear']],
            ['fonts', []],
            ['color', []],
            ['undo', []],
            ['ckMedia', []],
            ['misc', ['link', 'picture','codeview']],
            ['para', []],
            ['height', []],
        ];

    $('#'+id).materialnote({
        toolbar: toolbar,
        height: 100,
        minHeight: 100,
        defaultBackColor: '#fff'
    });
}

function inicializarEditorPorClase(clase){
    var toolbar = [
            ['style', []],
            ['fonts', []],
            ['color', []],
            ['undo', []],
            ['ckMedia', []],
            ['misc', ['link', 'picture','codeview']],
            ['para', []],
            ['height', []],
        ];

    $(clase).materialnote({
        toolbar: toolbar,
        height: 100,
        minHeight: 100,
        defaultBackColor: '#fff'
    });
}