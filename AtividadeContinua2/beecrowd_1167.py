ano1 = int(input())
ano2 = int(input())
cont = 0
if ano1 >= 0 and ano2 <= 9999: 
    for list in range(ano1, ano2 + 1):
        if list % 100 != 0 and list % 4 == 0 or list % 400 == 0:
            print(list)
            cont +=1
print(f'bissextos: {cont}')
