preco = float(input())
qtdcompra = int(input())
valortotal = preco * qtdcompra
desc = 10 + qtdcompra

calculodesc = desc * valortotal
valordesc = calculodesc / 100

precofinal = valortotal - valordesc

print(f'{valortotal:.2f}\n{precofinal:.2f}')
