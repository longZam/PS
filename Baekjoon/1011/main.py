T = int(input())

for case in range(T):
    x, y = map(int, input().split())
    y -= x
    z = 1
    sum = 0
    
    while (y > sum + z * 2):
        sum += z * 2
        z += 1
    
    if sum + z >= y:
        print(f"{2*z-1}")
    else:
        print(f"{2*z}")