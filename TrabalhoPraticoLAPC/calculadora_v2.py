saida = ''
#Funções matemáticas
def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0 or a == 0:
        return('Não foi possível realizar a divisão por 0')
    else:
        return a / b
#Função calculadora
def calculadora(num1, num2, operacao):
    operacao = operacao.lower()

    if operacao in ('+', 'adição', 'adicao'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtração', 'subtracao'):
        resultado = subtracao(num1, num2)
    elif operacao in ('*', 'multiplicação', 'multiplicacao'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisão', 'divisao'):
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    return resultado
#Laço while 
while saida.lower() != 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação desejada: ')
    resultado = calculadora(num1, num2, operacao)
    print(f'Resultado da operação: ', resultado)

    saida = input('Deseja realizar outra operação ? (S/N): ')
    
    

    
