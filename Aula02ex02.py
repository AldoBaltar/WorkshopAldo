

class Calculadora:
    def __init__(self, x, y):
            self.num1 = x
            self.num2= y

    def main(self):
        print("""
[1] Soma
[2] Subtração 
[3] Multiplicação
[4] Divisão
[5] Encerrar
    """)
        base = int(input('Digite a operação desejada: '))
        x = float(input('Digite um numero: '))
        y = float(input('Digite outro numero: '))
        print(f'A {op} de {x} e {y}')

    def soma(self):
        print(self.num1 +  self.num2)
        
    def subtracao(self):
        print(self.num1 -  self.num2)
    
    def multiplicacao(self):
        print(self.num1 *  self.num2)
    
    def divisao(self):
        print(self.num1 /  self.num2)


p1 = Calculadora
p1.main()
