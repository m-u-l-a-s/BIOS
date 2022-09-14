
const submit = document.getElementById("submit");
const storage = window.localStorage;
const d = new Date();
semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
let ordens = []

function cleanField() {
    document.getElementById("lab").value = "";
    document.getElementById("maq").value = "";
    document.getElementById("prob").value = "";
}

function getData() {
    let lab = document.getElementById("lab")
    let maq = document.getElementById("maq")
    let prob = document.getElementById("prob")
    ordens.push(lab.value, maq.value, prob.value)
    storage.setItem("lab", lab.value)
    storage.setItem("maq", maq.value)
    storage.setItem("prob", prob.value)
    console.log(ordens)
    cleanField()
}

function createOS() {
    let conteudo = document.getElementById("conteudo");
    let os = document.createElement("div")
    os.className = "ordem-servico"
    let lab = document.createElement("p")
    let maq = document.createElement("p")
    let prob = document.createElement("p")
    let status = document.createElement("p")
    let date = document.createElement("p")

    let dia = `${semana[d.getDay()]}, ${d.getDate()} de ${ano[d.getMonth()]} de ${d.getFullYear()} às ${d.getHours()} horas e ${d.getMinutes()} minutos.`
    let resolvido = document.createElement("button")
    resolvido.innerText = "Resolvido!"
    let excluir = document.createElement("button")
    excluir.innerText = "Excluir"

    lab.textContent = "Laboratório: "+storage.getItem("lab")
    maq.textContent = "Máquina: "+storage.getItem("maq")
    prob.textContent = "Problema: "+storage.getItem("prob")
    status.textContent = "Status: Pendente"
    date.textContent = "Reportado em: "+dia

    os.appendChild(lab)
    os.appendChild(maq)
    os.appendChild(prob)
    os.appendChild(status)
    os.appendChild(date)
    os.appendChild(excluir)
    os.appendChild(resolvido)
    conteudo.appendChild(os)

}

submit.addEventListener("click", getData)