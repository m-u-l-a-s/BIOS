
const submit = document.getElementById("submit");
const storage = window.localStorage;

const d = new Date();
semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

// Aqui serão armazenados objetos com as infos das ordens de serviço
let ordens = JSON.parse(storage.getItem("ordens")) || []

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
    let os = {
        "lab": lab,
        "maq": maq,
        "prob": prob,
        "rep": dia
    };
    ordens.push(os)
    let tmp = JSON.stringify(ordens)
    storage.setItem("ordens", tmp)
    cleanField()
}

function createOS() {
    let divConteudo = document.getElementById("conteudo");
    let osArr = JSON.parse(storage.getItem("ordens"))
    console.log(osArr)
    
    // Create HTML elements:
    osArr.forEach(ordem => {
        
        let divOrdem = document.createElement("div");
        divOrdem.setAttribute("class", "ordem-servico")
        let ul = document.createElement("ul")
        let lab = document.createElement("li")
        let maq = document.createElement("li")
        let prob = document.createElement("li")
        let status = document.createElement("li")
        let date = document.createElement("li")
    
        // Get data from localStorage:
        lab.textContent = "Laboratório: "+ ordem.lab
        maq.textContent = "Máquina: "+ordem.maq
        prob.textContent = "Problema: "+ordem.prob
        date.textContent = "Reportado em: " + ordem.rep
        status.textContent = "Status: pendente."
    
        let resolvido = document.createElement("button")
        resolvido.innerText = "Resolvido!"
    
        ul.appendChild(lab)
        ul.appendChild(maq)
        ul.appendChild(prob)
        ul.appendChild(date)
        ul.appendChild(resolvido)
        divOrdem.appendChild(ul)
        divConteudo.appendChild(divOrdem)

    })



}

submit.addEventListener("click", getData)