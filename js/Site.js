// Initialize collapse button
$(".dropdown-button").dropdown();
$(".button-collapse").sideNav();
$('select').material_select();
$('.modal-trigger').leanModal();
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