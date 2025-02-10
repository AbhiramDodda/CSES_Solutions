'''
Given a string, your task is to reorder its letters in such a way that it becomes a palindrome.
'''

s = input()
def solve(s):
    n = len(s)
    cnts = [0]*26
    for i in s:
        cnts[ord(i) - ord('A')] += 1
    odds = 0
    for i in cnts:
        if i%2 == 1:
            odds += 1
    if odds > 1:
        return "NO SOLUTION"
    if n%2 == 0 and odds == 1:
        return "NO SOLUTION"
    odd = ""
    temp1 = ""
    temp2 = ""
    for i in range(26):
        l = chr(ord('A') + i)
        if cnts[i]%2 == 1:
            for j in range(cnts[i]):
                odd += l
            continue
        for j in range(cnts[i]//2):
            temp1 += l
            temp2 += l
    if n%2 == 0:
        for i in range(len(temp2)-1, -1, -1):
            temp1 += temp2[i]
        return temp1
    else:
        temp1 += odd
        for i in range(len(temp2)-1, -1, -1):
            temp1 += temp2[i]
        return temp1
print(solve(s))