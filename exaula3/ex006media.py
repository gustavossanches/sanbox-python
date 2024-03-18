alunos = int(input('Digite o número de alunos na turma: '))
i = 1
soma = 0
media = 0

while i < alunos+1:
    nota = float(input(f'Digite a nota do °{i} aluno: '))
    soma += nota
    media = soma/i
    
    i = i + 1
    
print(f'A média da turma é igual a {media}!')