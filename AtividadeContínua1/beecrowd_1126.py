data_compra = str(input())
prazo = int(input())

dias_semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
dia_entrega = None
if (prazo == 0):
    print('chega hoje!')
else:
    indice_atual = dias_semana.index(data_compra)
    while prazo > 0:
        if indice_atual == len(dias_semana) - 1:
            indice_atual = 0
        else:
            indice_atual += 1
        prazo -= 1
    dia_entrega = dias_semana[indice_atual]
    print(f'sera entregue {dia_entrega}')



