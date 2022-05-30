doa = float(input())
total= 0.00
while doa > -1:
    total = total + doa
    doa = float(input())
print(f'VC$ {total:.2f}\nR$ {total*2.50:.2f}')