notatrab = float(input())
notaprova = float(input())
media = (notatrab + notaprova) / 2
if media >= 6.0:
    print('aprovado')
elif (notatrab + 10.0) / 2 >= 6.0:
    print('talvez com a sub')
else:
    print('reprovado')
