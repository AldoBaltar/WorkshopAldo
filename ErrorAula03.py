# Aqui estão todos os exercícios resolvidos, com o código quebrado, a explicação do erro e o código corrigido:

# ---

# ##  Nível 1 - Fácil

# ---

# ### Exercício 1: Identificando um Erro de Sintaxe

# **Código quebrado:**

# ```python
# print("Olá, mundo!"
# ```

# ** Anotações:**

# - **Erro:** `SyntaxError: unexpected EOF while parsing`
# - **Causa:** O parêntese de fechamento da função `print()` está faltando. O Python chegou ao fim do arquivo esperando ainda fechar o parêntese.
# - **O que aconteceu:** O interpretador Python leu `print("Olá, mundo!"` e esperava um `)` para fechar a chamada da função, mas encontrou o fim do arquivo antes disso.

# **Código corrigido:**

# ```python
# print("Olá, mundo!")
# ```

# ---

# ### Exercício 2: Lidando com um NameError

# **Código quebrado:**

# ```python
# print(nome)
# ```

# ** Anotações:**

# - **Erro:** `NameError: name 'nome' is not defined`
# - **Causa:** A variável `nome` está sendo usada sem ter sido definida anteriormente.
# - **O que aprendi (via pesquisa):** Um `NameError` ocorre quando o Python não encontra o nome de uma variável, função ou módulo no escopo atual. Isso acontece quando tentamos usar algo antes de defini-lo ou quando erramos o nome de uma variável.

# **Código corrigido:**

# ```python
# nome = "Aldo"
# print(nome)
# ```

# ---

# ##  Nível 2 - Médio

# ---

# ### Exercício 3: Erro de Tipagem (TypeError)

# **Código quebrado:**

# ```python
# def somar(a, b):
#     return a + b

# resultado = somar(10, "5")
# print(resultado)
# ```

# ** Anotações:**

# - **Erro:** `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
# - **Causa:** A função tenta somar um inteiro (`10`) com uma string (`"5"`), o que não é permitido diretamente em Python.
# - **Solução:** Usamos `try-except` para capturar o `TypeError` e, dentro do `except`, convertemos os argumentos para o mesmo tipo antes de somar.

# **Código corrigido:**

# ```python
# def somar(a, b):
#     try:
#         return a + b
#     except TypeError:
#         print(f"Erro de tipo: não é possível somar '{type(a).__name__}' com '{type(b).__name__}'. Convertendo para números...")
#         return float(a) + float(b)

# resultado = somar(10, "5")
# print(resultado)
# ```

# ---

# ### Exercício 4: Corrigindo um Erro de Índice (IndexError)

# **Código quebrado:**

# ```python
# numeros = [10, 20, 30]
# indice = int(input("Digite um índice para acessar a lista: ")) 

# print(numeros[indice])
# ```

# ** Anotações:**

# - **Erro:** `IndexError: list index out of range` (ao digitar um índice maior que 2 ou menor que -3)
# - **Causa:** A lista `numeros` tem apenas 3 elementos (índices 0, 1 e 2). Qualquer índice fora desse intervalo causa o erro.
# - **Solução:** Validamos o índice antes de acessar a lista e usamos `try-except` para garantir que o programa não quebre.

# **Código corrigido:**

# ```python
# numeros = [10, 20, 30]

# try:
#     indice = int(input("Digite um índice para acessar a lista (0 a 2): "))
    
#     if indice < 0 or indice >= len(numeros):
#         print(f"Índice inválido! A lista tem apenas {len(numeros)} elementos (índices de 0 a {len(numeros)-1}).")
#     else:
#         print(numeros[indice])

# except ValueError:
#     print("Erro: você deve digitar um número inteiro válido.")
# except IndexError:
#     print("Erro: índice fora dos limites da lista.")
# ```

# ---

# ### Exercício 5: Tratando Múltiplos Erros ao Mesmo Tempo

# **Código quebrado:**

# ```python
# def dividir(a, b):
#     return a / b

# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ")

# resultado = dividir(int(num1), int(num2))
# print(f"Resultado: {resultado}")
# ```

# ** Anotações:**

# - **Erros possíveis:**
#     1. `ValueError` — se o usuário digitar texto em vez de número (ex: `"abc"`)
#     2. `ZeroDivisionError` — se o segundo número for zero
# - **Solução:** Capturamos cada erro separadamente com múltiplos blocos `except`, exibindo mensagens adequadas para cada caso.

# **Código corrigido:**

# ```python
# def dividir(a, b):
#     return a / b

# try:
#     num1 = input("Digite o primeiro número: ")
#     num2 = input("Digite o segundo número: ")

#     resultado = dividir(int(num1), int(num2))
#     print(f"Resultado: {resultado}")

# except ValueError:
#     print("Erro: você deve digitar apenas números inteiros válidos. Não use letras ou símbolos.")
# except ZeroDivisionError:
#     print("Erro: não é possível dividir por zero. Digite um segundo número diferente de 0.")
# ```

# ---

# ##  Nível 3 - Difícil

# ---

# ### Exercício 6: Erro ao Trabalhar com Dicionários

# **Código quebrado:**

# ```python
# dados = {
#     "nome": "Isaac ",
#     "idade": 25,
#     "cidade": "São Paulo"
# }

# chave = input("Digite a chave que deseja acessar: ")

# print(f"O valor da chave '{chave}' é: {dados[chave]}")
# ```

# **    Anotações:**

# - **Erro:** `KeyError: 'endereco'` (exemplo ao digitar uma chave inexistente)
# - **Causa:** O código tenta acessar `dados[chave]` diretamente. Se a chave não existir no dicionário, o Python lança um `KeyError`.
# - **Sobre o método `get()`:** `dados.get("endereco", "Endereço não encontrado")` retorna o valor se a chave existir, ou o valor padrão fornecido caso não exista — sem lançar exceção. É a forma mais Pythonica de evitar `KeyError`.

# **Código corrigido (versão com `try-except`):**

# ```python
# dados = {
#     "nome": "Isaac",
#     "idade": 25,
#     "cidade": "São Paulo"
# }

# chave = input("Digite a chave que deseja acessar: ")

# try:
#     print(f"O valor da chave '{chave}' é: {dados[chave]}")
# except KeyError:
#     print(f"Erro: a chave '{chave}' não existe no dicionário. Chaves disponíveis: {list(dados.keys())}")
# ```

# **Código corrigido (versão com `get()` — mais elegante):**

# ```python
# dados = {
#     "nome": "Isaac",
#     "idade": 25,
#     "cidade": "São Paulo"
# }

# chave = input("Digite a chave que deseja acessar: ")

# valor = dados.get(chave, f"Chave '{chave}' não encontrada no dicionário.")
# print(f"O valor da chave '{chave}' é: {valor}")
# ```

# ---

# ### Exercício 7: Criando um Erro Personalizado

# **Código quebrado:**

# ```python
# def validar_idade(idade)
#     if idade < 0 or idade > 120:
#         raise ValueError("A idade deve estar entre 0 e 120 anos!")
#     return f"Idade válida: {idade}"

# idade = int(input("Digite sua idade: "))
# print(validar_idade(idade))
# ```

# ** Anotações:**

# - **Erro 1 (Sintaxe):** `SyntaxError` — falta o `:` no final da definição da função `def validar_idade(idade)`.
# - **Erro 2 (em tempo de execução):** Se o usuário digitar uma idade inválida (ex: `-5` ou `200`), o `ValueError` personalizado é lançado mas não é capturado, encerrando o programa.
# - **Solução:** Corrigimos o `:` na definição e adicionamos `try-except` + loop `while` para que o programa continue pedindo até receber um valor válido.

# **Código corrigido:**

# ```python
# def validar_idade(idade):
#     if idade < 0 or idade > 120:
#         raise ValueError("A idade deve estar entre 0 e 120 anos!")
#     return f"Idade válida: {idade}"

# while True:
#     try:
#         idade = int(input("Digite sua idade: "))
#         resultado = validar_idade(idade)
#         print(resultado)
#         break  # Sai do loop quando a idade é válida
#     except ValueError as e:
#         print(f"Entrada inválida: {e}. Tente novamente.")
# ```

# ---

# ##  Desafio Extra: Debugando um Código com Múltiplos Erros

# **Código quebrado:**

# ```python
# def calcular_media(notas):
#     soma = sum(notas)
#     quantidade = len(notas)
#     return soma / quantidade

# notas = [8, 9, "10", 7]
# media = calcular_media(notas)
# print(f"Média: {media:.2f}")
# ```

# ** Anotações:**

# - **Erro 1 — `TypeError`:** A lista `notas` contém `"10"` como string. A função `sum()` não consegue somar inteiros com strings.
# - **Erro 2 — `ZeroDivisionError` (potencial):** Se a lista `notas` estiver vazia, `len(notas)` será `0` e ocorrerá divisão por zero.
# - **Erro 3 — Entrada do usuário não validada:** Se adaptarmos para aceitar entradas do usuário, precisamos garantir que sejam números válidos.
# - **Solução pesquisada no Stack Overflow:** Usar `map(int, lista)` converte todos os elementos de uma lista de strings para inteiros. Checar `if not notas` antes de dividir evita o `ZeroDivisionError`.

# **Código corrigido (lista fixa):**

# ```python
# def calcular_media(notas):
#     if not notas:
#         raise ValueError("A lista de notas está vazia. Não é possível calcular a média.")
    
#     # Converte todos os elementos para float, mesmo que sejam strings numéricas
#     notas_convertidas = list(map(float, notas))
#     soma = sum(notas_convertidas)
#     quantidade = len(notas_convertidas)
#     return soma / quantidade

# notas = [8, 9, "10", 7]
# media = calcular_media(notas)
# print(f"Média: {media:.2f}")
# ```

# **Código adaptado para entrada do usuário:**

# ```python
# def calcular_media(notas):
#     if not notas:
#         raise ValueError("A lista de notas está vazia. Não é possível calcular a média.")
    
#     notas_convertidas = list(map(float, notas))
#     soma = sum(notas_convertidas)
#     quantidade = len(notas_convertidas)
#     return soma / quantidade

# notas = []
# quantidade = int(input("Quantas notas você quer inserir? "))

# for i in range(quantidade):
#     while True:
#         try:
#             nota = input(f"Digite a nota {i+1}: ")
#             notas.append(float(nota))  # Valida e converte
#             break
#         except ValueError:
#             print("Valor inválido. Digite apenas números.")

# try:
#     media = calcular_media(notas)
#     print(f"Média: {media:.2f}")
# except ValueError as e:
#     print(f"Erro: {e}")
# ```