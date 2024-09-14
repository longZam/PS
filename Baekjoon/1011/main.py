# 해당 속도에서 감속시켜서 속도 1까지 도달할 때까지의 이동 거리
# 현 속도가 4, 이 상태에서 감속시켜서 1까지 도달하면 이동 거리는
# 4 + 3 + 2 + 1 = 10
def gause_sum(n: int):
    return n * (n + 1) / 2

T = int(input())

for case in range(T):
    x, y = map(int, input().split())
    remain_dist = y - x
    move_dist = 1
    result = 0

    while remain_dist > 0:
        # 이동 횟수 세기
        result += 1
        # 남은 거리 갱신
        remain_dist -= move_dist

        # 현 속도를 다음까지 유지한 후 감속시켰을 때 남는 거리를 평가
        evaluation = remain_dist - gause_sum(move_dist)

        # 현 속도 유지 시 남은 거리가 증가한 속도보다 크거나 같으면 올려도 괜찮음
        if evaluation >= move_dist + 1:
            move_dist += 1
        # 현 속도 유지 시 남은 거리가 음수면 감소시켜야 함
        elif evaluation < 0:
            move_dist -= 1
    
    print(result)