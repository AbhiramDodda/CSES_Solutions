'''
Your task is to count for k=1,2,...,n 
the number of ways two knights can be placed on a k x k chessboard so that they do not attack each other.
'''
n = int(input())
for i in range(1, n+1):
    if i == 1:
        print(0)
        continue
    temp = i**2
    any_two_positions = temp*(temp-1)//2 # nC2
    attacking_positions = 4*(i-1)*(i-2) # no.of 2x3 rectangles in ixi grid = 2*(i-1)*(i-3). *2 for knight positions in the rectangle
    print(any_two_positions - attacking_positions)