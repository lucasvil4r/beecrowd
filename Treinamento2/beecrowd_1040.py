x = input().split()
N1, N2, N3, N4 = x

media = (float(N1) * 2 + float(N2) * 3 + float(N3) * 4 + float(N4) * 1) / (2 + 3 + 4 + 1)

if media >= 7.0:
    aprov = 'Aluno aprovado.'
    print('Media: {:.1f}\n{}'.format(media, aprov))

if media >= 5.0 and media <= 6.9:
    aprov = 'Aluno em exame.'
    N5 = float(input())
    media2 = (media + N5) / 2

    if media2 >= 5.0:
        aprov2 = 'Aluno aprovado.'
    else:
        aprov2 = 'Aluno reprovado.'
    print('Media: {:.1f}\n{}\nNota do exame: {:.1f}\n{}\nMedia final: {:.1f}'.format(media, aprov, N5, aprov2, media2))


elif media < 5.0:
    aprov = 'Aluno reprovado.'
    print('Media: {:.1f}\n{}'.format(media, aprov))
