numcentro = int(input())
numleft = numcentro - 1
numright = numcentro + 1

if (numcentro >= 2):
    if (numleft % 2 == 1):
        numleft = numleft
    else:
        numleft = numleft - 1

    if (numright % 2 == 0):
        numright = numright
    else:
        numright = numright + 1

print(f'{numleft} {numright}')

