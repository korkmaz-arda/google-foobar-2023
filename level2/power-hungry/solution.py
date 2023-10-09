from functools import reduce
from operator import mul

def solution(xs):
    pos, neg = [], []
    # Separate positive and negative numbers
    for x in xs:
        if x < 0:
            neg.append(x)
        elif x > 0:
            pos.append(x)

    # Check edge cases
    if not pos:
        if 0 in xs:
            return "0"
        if not neg:
            return None
        elif len(neg) == 1:
            return str(neg[-1])            

    # Ensure the negative numbers are in doubles
    if len(neg) % 2 == 1:
        # If not, remove the number with the lowest abs value
        neg.remove(max(neg))

    # Find the products of items in each list
    pos_product = reduce(mul, pos) if pos else 1
    neg_product = reduce(mul, neg) if neg else 1
    
    # Comlexity is O(n)
    return str(pos_product * neg_product)