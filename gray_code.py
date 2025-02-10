'''
A Gray code is a list of all 2^n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).
Your task is to create a Gray code for a given length n.
'''

def gray_code(n):
    if n == 1:
        return ["0", "1"]
    prev = gray_code(n-1)
    prev_reverse = prev[::-1]
    prev_len = len(prev)
    i = 0
    while i < prev_len:
        append0 = "0" + prev[i]
        prev[i] = "1" + prev_reverse[i]
        prev.append(append0)
        i += 1
    return prev

n = int(input())
ans = gray_code(n)
for i in ans:
    print(i)