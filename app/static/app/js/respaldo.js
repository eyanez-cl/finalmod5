
$(function (){
    $("#boton-js").click(function(){
        $.ajax({
            url:'/crearexamen/',
            type:'get',
            dataType: 'json',
            beforeSend:function(){
                $("#modal-form").modal("show");
            },
            success: function(data){
                $("#modal-form .modal-content").html(data.html_formulario);
            }
        })
    })

    $("#modal-form").on("submit",".js-create-form",function(){
        var form = $(this)
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success:function(data){
                console.log(data)
                if(data.formulario_is_valid){
                    $("#tabla-datos tbody").html(data.html_examenes_list)
                    $("#modal-form").modal("hide");
                }
                else{
                    $("#modal-form .modal-content").html(data.html_formulario)
                }
            }
        });
        return false;
    });
});