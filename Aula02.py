#Laço de Repetição
while True:
    a = input("Digite 'sair' para encerrar: ")
    
    if a.lower() == 'sair':
        print('Encerrado')
        break
    else:
        print(f'Você digitou errado: {a}')