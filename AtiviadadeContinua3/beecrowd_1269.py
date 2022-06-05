def exibir(lista):
    for item in lista:
        print(item, end=" ")

def adicionar(num):
    carrinho.append(num)

def remover(num):
    TesteLogico = num in carrinho
    if TesteLogico == True:
        carrinho.remove(num)
    else:
        print(f'código {num} não encontrado')

carrinho = input().split(" ")

'''
while acao == 'exibir' or acao == 'encerrar':

    if acao == 'exibir':
        exibir(carrinho)

    elif acao == 'encerrar':
        exibir(carrinho)
        break
'''
