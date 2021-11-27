total = 0
print(f'{" Números Primos ":=^50}')
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[36m', end='→ ')
        total += 1
    else:
        print('\033[31m', end='→ ')
    print(c, end='→ ')
print(f'\n\033[mO número {n} foi divisível {total} vezes.')
if total == 2:
    print('E por isso ele é um número PRIMO.')
else:
    print('Por isso ele NÃO é um número primo.')