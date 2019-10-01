def binarySearch(n, key):
    l = 1
    r = n

    cnt = 0

    while 1 :
        mid = int((l + r) / 2)
        cnt += 1

        if mid == key:
            break
        if mid < key:
            l = mid
        else :
            r = mid

    return cnt