num = int(input())
alfabeto = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cont = 1
if num >= 1 and num <=26:
    while cont <= num:
        letra = alfabeto[cont]
        letra_multletra = letra * cont
        print(letra_multletra)
        cont +=1