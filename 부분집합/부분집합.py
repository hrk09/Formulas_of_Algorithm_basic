# >> 연산은 오른쪽으로 1비트 밀 때마다 1/2씩 줄어듦
# 1 << m ; 2의 m승
# 1 >> m ; 1/2의 m승

def powerset(lst):
    x = len(lst)
    res = []
    # 부분집합개수
    for i in range(1<<x):
        # 만약 i의 j 번째 비트가 1이면 lst의 j번째 원소를 출력한다.
        # print([lst[j] for j in range(x) if i & (1<<j)])
        res.append([lst[j] for j in range(x) if i & (1<<j)])
    return res
print(powerset([3, 6, 7, 1, 5, 4]))

# 만약에 공백 값 없이 하고 싶다면,
def powerset2(lst):
    x = len(lst)
    # 부분집합개수
    for i in range(1, 1<<x):
        # 만약 i의 j 번째 비트가 1이면 lst의 j번째 원소를 출력한다.
        print([lst[j] for j in range(x) if i & (1<<j)])

powerset2([3, 6, 7, 1, 5, 4])