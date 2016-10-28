//----------------SLIDER PANTALLA PRINCIPAL--------------------//

$('.slider').slider({full_width: true});

//----------------DROPDOWN MENU PANTALLA PRINCIPAL--------------------//

$('.dropdown-button').dropdown();

//----------------BOTON COLLAPSE PANTALLA PRINCIPAL--------------------//

$('.button-collapse').sideNav();

//----------------MODAL PANTALLA PRINCIPAL--------------------//

$('.modal-trigger').leanModal();


function cerrarModal(id){
	$('#'+id).closeModal();

}
  $(document).ready(function(){
    $('.tooltipped').tooltip({delay: 50});

      $('#alternar-panel-oculto').toggle( 
        function(e){ 
            $('#panel-oculto').toggle( "slide" ,1000);

            $('#main').css({'padding-left': '0px'});
            $(this).find('i').text('menu');
            e.preventDefault();
        }, 
        function(e){ 
            $('#panel-oculto').toggle( "slide",1000);
            $('#main').css({'padding-left': '240px'});
            $(this).find('i').text('menu');
            e.preventDefault();
        }
    );
  });
     
      function showToast(message, duration){
         Materialize.toast(message, duration);
      }
      function showToast1(message, duration){
         Materialize.toast('<i>'+ message + '</i>', duration);
      }
      function showToast2(message, duration){
         Materialize.toast(message, duration, 'rounded');
      }
      function showToast3(message, duration){
         Materialize.toast('Hello World!', duration, '', function toastCompleted(){
               alert('Toast dismissed!');
            });
      }




   