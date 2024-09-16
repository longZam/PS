state = ''
str = input()
bundles = 0

for c in str:
    if state != c:
        state = c
        bundles += 1

print(bundles // 2)