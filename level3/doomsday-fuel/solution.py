import numpy as np
from fractions import Fraction

def inverse(m):
    return [[Fraction(item).limit_denominator() for item in row]
            for row in np.linalg.inv(np.array(m, dtype=np.float64))]

def solution(m):
    """    
    The input is an absorbing Markov chain.
    """
    start, n = 0, len(m)

    transit = [i for i, s in enumerate(m) if sum(s)]
    terminal = [i for i, s in enumerate(m) if not sum(s)]
    if 0 in terminal:
        return [1] + [0]*len(terminal[1:]) + [1]

    # Probability matrix:
    pm = [[int(i == j) if not sum(s) else Fraction(w, sum(s))
          for j, w in enumerate(s)]
          for i, s in enumerate(m)]

    R = [[pm[n][m]for m in terminal] for n in transit]
    Q = [[pm[n][m]for m in transit] for n in transit]
    I = np.eye(len(Q))
    F = inverse((I-Q)) # F = (I - Q)^(-1)
    FR = np.dot(F, R)

    dist = FR[start]
    denominator = np.lcm.reduce([n.denominator for n in dist])
    numerators = [n.numerator * (denominator/n.denominator) for n in dist]

    return numerators + [denominator]