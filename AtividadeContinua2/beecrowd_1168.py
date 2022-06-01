lower = int(input())
upper = int(input())
qtd = 0
lista = []
for num in range(lower,upper + 1):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			lista.append(num)
for list in lista:
    print(lista[qtd])
    qtd +=1
print(f'primos: {qtd}')
