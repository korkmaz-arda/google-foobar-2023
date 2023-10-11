def solution(l):
    # Create a dict where keys will map to their respective divisors
    divisors = {}
    for i, e in enumerate(l):
        divisors[(e, i)] = []

    # Find divisors of each number
    for i, e in enumerate(l):
        for j, n in enumerate(l[i+1:]):
            if n % e == 0:
                divisors[(n, j+i+1)].append((e, i)) #(value, index)

    # Calculate the number of triplets
    triplets = 0
    for num, div_num in divisors.items():
        for d in div_num:
            triplets += len(divisors[d])

    return triplets