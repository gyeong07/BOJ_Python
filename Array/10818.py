num1 = int(input())
num2 = []

for i in range(num1):
    num2.append(int(input()))

num2.sort()
print(num2[0], num2[len(num2)-1])
