s = input()
subString = ""
L = 0
R = 0
cnt = 0
B_string = []
for char in s:
    subString += char
    if char == "R":
        R += 1
    if char == "L":
        L += 1
    if L == R:
        cnt += 1
        B_string.append(subString)
        L = 0
        R = 0
        subString = ""
print(cnt)
for suBstring in B_string:
    print(suBstring)
