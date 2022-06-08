def exibir(lista):
    carrinho.sort(key=int)
    print(*lista)

def adicionar(num):
    carrinho.append(num)

def remover(num):
    TesteLogico = num in carrinho
    if TesteLogico == True:
        carrinho.remove(num)
    else:
        print(f'código {num} não encontrado')

def encerrar():
    carrinho.sort(key=int)
    exibir(carrinho)

carrinho = input().split(" ")
carrinho.sort()

while True:

    opcao = input().split(" ")
    acao = (opcao[0])
    
    if acao == 'exibir':
        exibir(carrinho)
    
    elif acao == 'adicionar':
        adicionar(opcao[1])

    elif acao == 'remover':
        remover(opcao[1])

    elif acao == 'encerrar':
        encerrar()
        break
