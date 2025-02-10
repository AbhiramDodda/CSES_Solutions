'''
A permutation of integers 1,2,...,n is called beautiful if there are no adjacent elements whose difference is 1.
Given n, construct a beautiful permutation if such a permutation exists.
'''
n = int(input())
if n == 1:
    print("1")
elif n < 4:
    print('NO SOLUTION')
else:
    evens = [i for i in range(2, n+1) if i%2 == 0]
    odds = [i for i in range(1, n+1) if i%2 == 1]
    print(*evens, *odds)