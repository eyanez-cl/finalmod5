
const Azucar = document.getElementById('Azucar');
const Presion = document.getElementById('Presion');
const  PerfilRenal = document.getElementById('PerfilRenal');

const dataAzucar = [24,60,45,10,15,30]
const dataPresion = [13,25,40,36,14,42]
const dataRenal = [15,50,56,45,36,41]
const meses = ['Enero','Febrero','marzo','abril','mayo','junio']
const barType =  ['bar','line','pie']

function chars(id, datos,dataLabel,dataType){
    var ctx = id.getContext('2d');
     new Chart(ctx, {
        type: dataType,
        data: {
            labels: dataLabel,
            datasets: [{
                label: '% de muestras',
                data: datos,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
   chars(Azucar,dataAzucar,meses,barType[0]);
   chars(Presion,dataPresion,meses,barType[1]);
   chars(PerfilRenal,dataRenal,meses,barType[2]);

});