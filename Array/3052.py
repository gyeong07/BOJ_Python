# num = []
# temp = []
# count = 0

# for i in range(0, 10):
#     num.append(int(input()) % 42)

# for i in range(0, 10):
#     if num[i] != 0:

num = []

for i in range(0, 10):
    num.append(int(input()) % 42)

num.sort()

temp = set(num)

print(len(temp))
