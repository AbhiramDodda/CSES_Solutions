'''
You are given all numbers between 1,2,...,n except one. Your task is to find the missing number.
'''
n = int(input())
nums = list(map(int, input().split()))
ref = sum(nums)
original_sum = (n*(n+1))//2
missing_num = original_sum - ref
print(missing_num)
''' Other solutions include nested loops(brute force) and using hashsets '''