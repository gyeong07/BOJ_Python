tc = int(input())
score = []

for i in range(tc):
    sNum = int(input())
    sum = 0
    ave = 0
    for j in range(sNum):
        score.append(int(input()))
        sum += score[j]

    ave = sum / sNum

    cnt = 0
    for k in range(sNum):
        if ave < score[k]:
            cnt += 1

    print(float(cnt) / float(sNum) * 100)
    score.clear()
