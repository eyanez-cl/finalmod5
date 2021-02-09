

const Email = document.getElementById('Email')
const pass = document.getElementById('Pass')
const boton = document.getElementById('Enviar')

const UserEmail = 'grupopython@gmail.com'
const password = '12345'


boton.addEventListener('click',(e)=>{
    e.preventDefault();
    if(Email.value === UserEmail && pass.value === password){
        window.location.replace("Privada.html");
    }
})

