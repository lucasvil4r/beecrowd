num = int(input())
num_impares = []

if (num >= 1 and num <= 1000):
    if (num % 2 == 0):
        for list in range(num - 1, 0, -2):
            num_impares.append(list)
            num_impares.sort(reverse = False)
    elif (num % 2 == 1):
        for list in range(num, 0, -2):
            num_impares.append(list)
            num_impares.sort(reverse = False)
for lista in num_impares:
    print(lista)
