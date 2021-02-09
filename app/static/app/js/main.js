
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