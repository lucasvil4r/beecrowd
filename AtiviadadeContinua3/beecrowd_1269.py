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
