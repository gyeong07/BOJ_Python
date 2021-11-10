a, b = input().split()

numa = int(a[::-1])
numb = int(b[::-1])

if numa > numb:
    print(numa)
else:
    print(numb)
