
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
                console.log(data)
            }
        })
    })
});

$(function (){
    $("#boton-js1").click(function (){
        $.ajax({
            url:'/agregar_usuario/',
            type:'get',
            dataType: 'json',
            beforeSend:function(){
                $("#modal-form").modal("show");
            },
            success: function(data){
                $("#modal-form .modal-content").html(data.html_formulario);
                console.log(data)
            }
        })
    })
});