ficha = []
while True:
    nome = str(input('Nome: ')) .upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    while resposta not in 'SN':
        resposta = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Ss':
        print('Pessoa adicionada!')
    elif resposta in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<5} {"NOME":<10} {"MÉDIA":<8}')
print('-'* 26)
for i, l in enumerate(ficha):
    print(f'{i:<5} {l[0]:<10} {l[2]:<8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('VOLTE SEMPRE!!!')
