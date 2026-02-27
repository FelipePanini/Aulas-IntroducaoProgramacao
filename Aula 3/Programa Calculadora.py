# Programa Calculadora Python
# Disciplina: Fundamentos de Programação
# Data: 26/02/2026


print("###########################################")
print("          Calculadora Python               ")
print("###########################################")

import math

print("Tecle a opção desejada e aperte ENTER: ")
print(" 1 - SOMA")
print(" 2 - SUBTRAÇÃO")
print(" 3 - MULTIPLICAÇÃO")
print(" 4 - DIVISÃO")
print(" 5 - POTENCIALIZAÇÃO")
print(" 6 - RAIZ QUADRADA")

op = input("Opção desejada: ")
op = int(op)

if op < 1 or op > 6:
	print("Insira uma opção entre 1 a 6! Encerrando o programa...")
	input()
	exit()

if (op == 6):
	a = input("Entre com o valor de A: ")
	a = int(a)
else:
	a = input("Entre com o valor de A: ")
	a = int(a)
	b = input("Entre com o valor de b: ")
	b = int(b)

if ( op == 1 ):
	print("A soma é: ", a+b )

elif ( op == 2 ):
	print("A subtração é: ", a-b )

elif ( op == 3 ):
	print("A multiplicação é: ", a*b )

elif ( op == 4 ):
	print("A divisão é: ", a/b )

elif ( op == 5 ):
	print("A potenciação é: ", a**b )

elif ( op == 6 ):
	print("A raiz quadrada é: ", math.sqrt (a))


input()