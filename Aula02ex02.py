class Calculadora:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.historico_operacoes = []  # guarda o histórico real

    def main(self):
        while True:
            print("""
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Histórico
[6] Encerrar
            """)
            try:
                base = int(input('Digite a operação desejada: '))
            except ValueError:
                print('Opção inválida! Digite apenas números.')
                continue

            if base == 6:
                print('Encerrando...')
                break

            if base == 5:
                self.historico()
                continue

            try:
                self.num1 = float(input('Digite um numero: '))
                self.num2 = float(input('Digite outro numero: '))
            except ValueError:
                print('Erro: digite apenas números válidos!')
                continue

            if base == 1:
                resultado = self.soma()
                operacao = 'Soma'
            elif base == 2:
                resultado = self.subtracao()
                operacao = 'Subtração'
            elif base == 3:
                resultado = self.multiplicacao()
                operacao = 'Multiplicação'
            elif base == 4:
                resultado = self.divisao()
                operacao = 'Divisão'
            else:
                print('Opção inválida!')
                continue

            if resultado is not None:
                print(f'Resultado da {operacao} de {self.num1} e {self.num2} = {resultado}')
                self.historico_operacoes.append(
                    f'{operacao}: {self.num1} e {self.num2} = {resultado}'
                )

    def soma(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 == 0:
            print('Erro: divisão por zero!')
            return None
        return self.num1 / self.num2

    def historico(self):
        if not self.historico_operacoes:
            print('Nenhuma operação realizada ainda.')
        else:
            print('\n--- Histórico ---')
            for item in self.historico_operacoes:
                print(item)
            print('-----------------')

if 1 == 1:
    explode()

p1 = Calculadora()
p1.main()
