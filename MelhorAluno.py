#faça um codigo que leia quantos alunos tem na sala e mande o usuario digitar o nome e nota de cada um 
# e diga o nome do aluno que tirou a nota mais alta.
print('-' * 25)
print('Escola Sou Frida')
print('-' * 25)

contador = 0
maior = 0
nota = 0
melhorA = ''

alunos = int(input('Quantos alunos a turma tem? '))
while contador < alunos:
    contador = contador + 1
    nome = input(f'Nome do  {contador}º alune: ')
    nota = int(input(f'Nota de {nome}: '))
    if nota >  maior:
        maior = nota
        MelhorA = nome

    
print(f'A nota mais alta foi {maior} de {MelhorA}.')

