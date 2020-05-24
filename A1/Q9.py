from math import sqrt


def factorsof(num):
    """return an array of factors of num"""
    factors = []
    factors.append(1)
    factors.append(num)

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            other_factor = num // i

            # in case of perfect squares
            if i == other_factor:
                factors.append(i)
            else:
                factors.extend([i, other_factor])

    return factors


def is_harmonic_divisor_number(num):
    """
    harmonic divisor numbers have the harmonic mean
    of all their divisors as an integer
    """

    hm = 0
    factors = factorsof(num)

    for i in factors:
        hm += 1 / i

    hm = len(factors) / hm
    hm = round(hm, 5)           # get precision upto 5th decimal place

    if hm.is_integer():
        return True
    return False


if __name__ == "__main__":
    i = 1
    num_hdn_found = 0

    while num_hdn_found < 10:
        if is_harmonic_divisor_number(i):
            print(i)
            num_hdn_found += 1
        i += 1
