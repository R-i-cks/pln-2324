
function delete_conceito(designacao){ 

$.ajax({
    url: '/conceitos/' + designacao,
    type: 'DELETE',
    success: function(result){
        // Algo c o result
        alert('deleted')
        window.location.href = '/conceitos';
    }
});

}

$(document).ready( function () {
    $('#dados').DataTable();
} );

$(document).ready(function(){
    $("#pesquisa").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#res .entrada").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });