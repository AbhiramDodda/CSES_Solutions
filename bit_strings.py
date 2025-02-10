'''
Your task is to calculate the number of bit strings of length n.
For example, if n=3, the correct answer is 8, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.
'''

n = int(input())
ans = 2
mod = 10**9+7
for i in range(1, n):
    ans = (ans%mod * 2)%mod # for each bit there are 2 possibilities either 0 or 1.
print(ans)