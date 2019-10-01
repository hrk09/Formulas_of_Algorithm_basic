import sys
sys.stdin = open('input.txt', 'r')

# 이진탐색 함수 정의(while문)
def cnt_bin(p, goal):
    cnt = 0
    start = 1

    # 찾을때까지 돌림
    while True:
        # 중간값 갱신
        mid = (start + p) // 2
        cnt += 1
        # 찾으면 break하고 while문 빠져나감
        if mid == goal:
            break
        # goal 값이 중간값보다 크면 시작값 조정
        elif mid < goal:
            start = mid
        else:
            p = mid
    return cnt


TC = int(input())
for t in range(1, TC+1):
    # 값 받기
    p, pa, pb = map(int, input().split())
    cnt_a = cnt_bin(p, pa)
    cnt_b = cnt_bin(p, pb)
    if cnt_a > cnt_b:
        print('#{} B'.format(t))
    elif cnt_a < cnt_b:
        print('#{} A'.format(t))
    else:
        print('#{} 0'.format(t))