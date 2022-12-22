s=input()
print(*[s.count(chr(a+ord('a'))) for a in range(26)])