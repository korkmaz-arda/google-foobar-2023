from decimal import Decimal, getcontext


getcontext().prec = 102
sqrt2 = Decimal(2).sqrt()


def beatty_sum(n):
    # Returns the sum of a Beatty sequence where the irrational term is square root 2
    if 1 == n:
        return 1
    if 1 > n:
        return 0

    A = int((sqrt2 - 1) * 10**100)
    N = (A * n) // 10**100
    return sum((
        n * (n + 1) // 2,
      - N * (N + 1) // 2,
      + N * n,
      - beatty_sum(N)
    ))


def solution(n):
    return str(beatty_sum(int(n)))