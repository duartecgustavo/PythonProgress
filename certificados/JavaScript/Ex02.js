// Desafio 2 - Programa que  çeias 4 notas de um aluno. Deposi mostre apresente se ete aluno foi 'Aprovado' ou 'Reprovado'

// entrada

let nome =  prompt('Seu nome: ')

let nota1 = Number(prompt('Primeira nota: '))
let nota2 = Number(prompt('Segunda nota: '))
let nota3 = Number(prompt('Terceira nota: '))
let nota4 = Number(prompt('Quarta nota: '))

// processamento

let media = (nota1 + nota2 + nota3 + nota4) / 4

// saída

if (media >= 7) {
	document.write(`Você foi aprovado! Sua media é ${media}!`)
}
else {
	document.write(`Achou que ia passar de ano? Achou errado otário!!! Vai estudar pq sua média foi ${media}`)
}
