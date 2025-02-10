'''
Your task is to divide the numbers 1,2,...,n into two sets of equal sum.

'''

n = int(input())
total = (n*(n+1))//2
# if the sum id not even then it is not possible to divide the sequence as it consists of integers.
if total%2 != 0:
    print("NO")
else:
    # elements of both the sets must have equal sum i.e total/2
    print("YES")
    s1, s2 = [], []
    check = [0]*(n+1)
    s1_sum = 0
    maxe = n

    while s1_sum < total//2:
        remaining = total//2 - s1_sum

        if remaining > maxe:
            s1.append(maxe)
            check[maxe] = 1
            s1_sum += maxe
            maxe -= 1
        else:
            s1.append(remaining)
            check[remaining] = 1
            s1_sum = total//2

    for i in range(1, n+1):
        if check[i] == 0:
            s2.append(i)
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)