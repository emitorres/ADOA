// Initialize collapse button
//$(document).ajaxStart($.blockUI).ajaxStop($.unblockUI);
$(document).ready(function(){
    $(".dropdown-button").dropdown();
    $(".button-collapse").sideNav();
    $('select').material_select();
    $('.modal-trigger').leanModal();
    $('.slider').slider({full_width: true});
    $('.collapsible').collapsible({
          accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
        });
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
    height: 300,
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