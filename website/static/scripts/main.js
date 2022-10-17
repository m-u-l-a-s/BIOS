const submit = document.getElementById("submit");
const storage = window.localStorage;
const labo = document.getElementById("lab");

d = new Date();

semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

// Aqui serão armazenados objetos com as infos das ordens de serviço
let ordens = JSON.parse(storage.getItem("ordens")) || []
let resolvidos = JSON.parse(storage.getItem("resolvidos")) || []

labo.addEventListener("change", changeImg)
function changeImg()
{
    document.getElementById("btn_img").click();
}

function cleanField() {
    document.getElementById("lab").value = "";
    document.getElementById("maq").value = "";
    document.getElementById("prob").value = "";
}

function getData() {
    let dia = `${semana[d.getDay()]}, ${d.getDate()} de ${ano[d.getMonth()]} de ${d.getFullYear()} às ${d.getHours()} horas e ${d.getMinutes()} minutos.`
    let lab = document.getElementById("lab").value
    let maq = document.getElementById("maq").value
    let prob = document.getElementById("prob").value
    
    // Criando objeto da Ordem de Serviço:
    let os = {
        "lab": lab,
        "maq": maq,
        "prob": prob,
        "rep": dia,
        "stat": false
    };

    ordens.push(os)
    let tmp = JSON.stringify(ordens)
    storage.setItem("ordens", tmp)
    //cleanField()
}

submit.addEventListener("click", getData)
