n = int(input())
ar = list(map(int, input().split()))
cnt = 0
while True:
    if all(x % 2 == 0 for x in ar):
        ar = [x // 2 for x in ar]
        cnt += 1
    else:
        break
print(cnt)
