saldo = 0
trans = 0
while True:
    print("""        [1] Depósito
        [2] Saque 
        [3] Extrato
        [4] Sair""")
    
    base = int(input('Digite uma opção: '))
    if base == 1:
        add = float(input('Digite o quanto você quer depositar: '))
        print(f'Você depositou: {add}')
        saldo += add
        trans += 1
        print(f'Seu saldo é de: {saldo}')

    elif base == 2:
        sub = float(input('Digite o valor do saque: '))
        if sub > saldo:
            print('Saldo insuficiênte')
            break
        print(f'Você sacou: {sub}')
        saldo -= sub
        trans += 1
        print(f'Seu saldo atual é de: {saldo}')

    elif base == 3:
        print(f'O total de transações é de: {trans}')

    elif base == 4:
        print('Encerrado')
        break
    else:
        print('Digite uma das opções.')
        break