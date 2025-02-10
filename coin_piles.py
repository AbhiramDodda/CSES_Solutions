''' 
You have two coin piles containing a and b coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, 
or two coins from the left pile and one coin from the right pile. Your task is to efficiently find out if you can empty both the piles.
'''

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    # x + 2y = a
    # 2x + y = b
    # solutions are x = (2b-a)/3 and y = (2a-b)/3
    if (2*a - b)%3 != 0 or (2*a - b) < 0 or (2*b - a)%3 != 0 or (2*b - a) < 0:
        print("NO")
    else:
        print("YES")