import numpy as np
from fractions import Fraction

def inverse(m):
    return [[Fraction(item).limit_denominator() for item in row]
            for row in np.linalg.inv(np.array(m, dtype=np.float64))]

def solution(m):
    """    
    The input is an absorbing Markov chain.

    To solve AMCs, we will:
    1) Separate terminal(absorbing) and transitionary states.
    
    2) Get the probability matrix with probabilities as fractions.
        (NOT decimal fractions!)
    
    3) Find sub matrices R and Q.
        R contains moves where the Markov chain finally stops at a terminal state.
        Q contains moves where the chain moves from one trasitionary state to an another.

        Note: Since we've already separated terminal and transitionary 
              states, we don't really need to order the probability matrix.

    4) Find the fundamental matrix, F, for the probability matrix.
        F contains information about the expected number of times (in fractions) the 
        process visits each transient state starting at a specific transient state

        The element F(i, j) represents the expected number of times (in fractions) 
        the process visits transient state j starting from transient state i.

    5) Find the product of F and R.
        This gives us a matrix that contains the expected number of visits 
        (in fractions) to each absorbing state from each transient state.

        The element FR(i, j) represents the expected number of times (in fractions) the 
        process visits absorbing state j starting from transient state i before being absorbed.

    6) Find the probability distribution of terminal states for the 
       starting state and return the output in requested format.
    """
    start, n = 0, len(m)

    transit = [i for i, s in enumerate(m) if sum(s)]
    terminal = [i for i, s in enumerate(m) if not sum(s)]
    if start in terminal:
        # Handle the edge case where starting state is absorbing
        return [0]*len(terminal[:start]) + [1] + [0]*len(terminal[start+1:]) + [1]

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