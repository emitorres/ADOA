// Initialize collapse button
$(".dropdown-button").dropdown();
$(".button-collapse").sideNav();
$('select').material_select();
$('.modal-trigger').leanModal();

function cambiarTab(tabContentId,tabId){
    $("#"+tabId).removeClass("disabled");
    $('ul.tabs').tabs('select_tab', tabContentId);
}