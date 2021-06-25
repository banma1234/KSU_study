def sangsu(a, b):
    a = a[::-1]
    b = b[::-1]
    if a>b:
        return a
    elif b>a:
        return b

a, b = input().split(' ')
print(sangsu(a, b))

