A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

questao_a = (A*C)/2
questao_b = pi * C * C
questao_c = (A + B) / 2.0 * C
questao_d = B * B
questao_e = A * B

print('TRIANGULO: {:.3f}'.format(questao_a))
print('CIRCULO: {:.3f}'.format(questao_b))
print('TRAPEZIO: {:.3f}'.format(questao_c))
print('QUADRADO: {:.3f}'.format(questao_d))
print('RETANGULO: {:.3f}'.format(questao_e))