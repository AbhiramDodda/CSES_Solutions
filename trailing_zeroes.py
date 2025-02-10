'''
Your task is to calculate the number of trailing zeros in the factorial n!.
For example, 20!=2432902008176640000 and it has 4 trailing zeros.
'''
n = int(input())
ref = 5
ans = 0
while ref <= n:
    ans += n//ref
    ref *= 5
print(ans)