from math import sqrt


def getSumOfFactors(num):
    """return the sum of perfect factors of num"""
    sum_of_factors = 1

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            other_factor = num // i

            # in case of perfect squares
            if i == other_factor:
                sum_of_factors += i
            else:
                sum_of_factors += i + other_factor

    return sum_of_factors


if __name__ == "__main__":
    pairs_found = []
    i = 4   # first non-prime

    while len(pairs_found) < 20:
        if i in pairs_found:
            i += 1
            continue

        sum_of_factors = getSumOfFactors(i)

        # perfect numers satisfy first condition, eg. 6
        if i != sum_of_factors and i == getSumOfFactors(sum_of_factors):
            pairs_found.extend([i, sum_of_factors])
            print(i, sum_of_factors)

        i += 1
