def xor(n):
    xor = n if not n % 2 else 0
    return xor + 1 * int(0 < n % 4 < 3)
    

def solution(start, length):
    checksum = 0
    n = start
    for i in range(length, 0, -1):
        checksum ^= xor(n+i-1)^xor(n-1)
        n += length

    return checksum