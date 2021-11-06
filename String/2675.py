testCnt = int(input())

for i in range(0, testCnt):

    inputS = input().split(' ')

    R = int(inputS[0])
    S = list(map(str, inputS[1]))

    for j in range(0, len(inputS[1])):
        print(S[j]*R, end='')
    print()
