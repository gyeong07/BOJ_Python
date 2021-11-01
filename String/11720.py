cnt = int(input())
num = list(input())
num_list = list(map(int, num))

sum = 0

for i in range(0, cnt):
    sum = sum + num_list[i]

print(sum)
