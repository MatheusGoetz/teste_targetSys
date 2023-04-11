num1 = int(0)
num2 = int(1)
num3 = int(0)

Valor = int(input('Digite um número: '))
while Valor > num3:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
if Valor == 0 or Valor == 1:
    print ('O número faz parte da sequência de Fibonacci.')
elif Valor == num3:
    print ('O número faz parte da sequência de Fibonacci.')
else:
    print ('O número digitado não faz parte da sequência de Fibonacci.')
