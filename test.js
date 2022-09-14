now = new Date()

semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

console.log(hj = `Hj é ${semana[now.getDay()]}, ${now.getDate()} de ${ano[now.getMonth()]} ${now.getFullYear()}`)