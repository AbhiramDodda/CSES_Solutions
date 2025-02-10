'''
You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
'''
dna = input()
ans = 0
ref = 1
for i in range(1, len(dna)):
    if dna[i] != dna[i-1]:
        ans = max(ans, ref)
        ref = 0
    ref += 1
ans = max(ans, ref)
print(ans)