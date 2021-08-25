tc = int(input())

for i in range(tc):
    cnt = 0
    sum = 0
    result = list(input())
    for j in range(len(result)):
        if(result.pop() == "O"):
            cnt += 1
        else:
            cnt = 0
        sum += cnt
    print(sum)
