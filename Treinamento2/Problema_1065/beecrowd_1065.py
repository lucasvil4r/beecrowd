num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

div1 = num1 % 2
div2 = num2 % 2
div3 = num3 % 2
div4 = num4 % 2
div5 = num5 % 2

cont = 0

if (div1 == 0):
    cont = cont + 1

if (div2 == 0):
    cont = cont + 1

if (div3 == 0):
    cont = cont + 1

if (div4 == 0):
    cont = cont + 1

if (div5 == 0):
    cont = cont + 1

print('{} valores pares'.format(cont))