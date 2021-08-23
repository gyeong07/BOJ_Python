num = int(input())
sum = 0
lst = []

for i in range(0, num):
    lst.append(int(input()))

lst.sort()

for i in range(0, num):
    lst[i] = lst[i]/lst[num-1]*100

for i in range(0, num):
    sum = sum+lst[i]

print(sum/num)
