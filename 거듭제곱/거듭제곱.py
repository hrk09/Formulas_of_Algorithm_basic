# 반복문 2의 k승
def power_of_2(k):
    i = 0
    res = 1
    # i 가 k보다 작을 때까지 돌림
    while i < k:
        res *= 2
        i += 1
    return res
print(power_of_2(3))

def power_of_4(k):
    i = 1
    res = 1
    # i 가 k+1이랑 같아지면 끝냄(3까지만 돌림)
    while i < k+1:
        res *= 4
        i += 1
    return res
print(power_of_4(3))

# 재귀호출
def power_of_3(m):
    if m == 0:
        return 1
    else:
        return 3 * power_of_3(m-1)
print(power_of_3(4))

