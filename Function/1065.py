def Han(num):

    if num < 100:
        return num
    else:
        cnt = 99
        for i in range(100, num+1):
            num_list = list(map(int, str(i)))
            if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
                cnt += 1
    return cnt


num = int(input())
print(Han(num))
