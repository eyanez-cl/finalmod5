
$(function () {

  /* Funciones */

  var cargarForm = function () {
    var btn = $(this);
    console.log(btn.attr)
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-form").modal("show");
      },
      success: function (data) {
        $("#modal-form .modal-content").html(data.html_formulario);
      }
    });
  };

  var guardarForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.formulario_is_valid) {
          $("#tabla-datos tbody").html(data.html_examenes_list)
          $("#modal-form").modal("hide");
        }
        else {
          $("#modal-form .modal-content").html(data.html_formulario)
        }
      }
    });
    return false;
  };


  /* Binding */

  // Crear Examen
  $("#boton-js").click(cargarForm);
  $("#modal-form").on("submit", ".js-create-form", guardarForm);



  // // Eliminar examen
  // $("#tabla-datos").on("click", ".js-delete", cargarForm);
  // $("#modal-form").on("submit", ".delete-examen", guardarForm);

});

