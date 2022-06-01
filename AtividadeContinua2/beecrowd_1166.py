divida = int(input())
pag = int(input())
numpag = 0
while  divida - pag > 0:
    sobra = divida - pag
    numpag +=1
    print(f'pagamento: {numpag}\nantes = {divida}\ndepois = {sobra}\n-----')
    divida = sobra
else:
    numpag +=1
    print(f'pagamento: {numpag}\nantes = {divida}\ndepois = {0}\n-----')
