'''
There is a pattern which you can observe in the example provided on the webpage.
'''
t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    m = max(y, x)
    ref_num = 1+m*(m-1) # diagonal numbers
    if x == y:
        print(ref_num)
    elif y < x:
        if m%2 == 0:
            print(ref_num-(m-y))
        else:
            print(ref_num+(m-y))
    else:
        if m%2 == 1:
            print(ref_num-(m-x))
        else:
            print(ref_num+(m-x))