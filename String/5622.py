alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0

word = input()

for unit in alp:
    for i in unit:
        for j in word:
            if i == j:
                cnt = cnt + alp.index(unit) + 3

print(cnt)
