from collections import Counter

n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
cntr = 0
for i, j in cnt.items():
    # print(i, j)
    if j > i:
        cntr += j - i
    if j < i:
        cntr += j
print(cntr)
