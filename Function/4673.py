def d(a):
    number = int(a)
    for i in list(str(a)):
        number += int(i)
    return number


not_self_num = []
for i in range(1, 10001):
    num = d(i)
    not_self_num.append(num)

for j in range(1, 10001):
    if j in not_self_num:
        pass
    else:
        print(j)
