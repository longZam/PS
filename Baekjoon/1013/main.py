import re

p = re.compile('(100+1+|01)+')

for i in range(int(input())):
    if p.fullmatch(input()):
        print("YES")
    else:
        print("NO")