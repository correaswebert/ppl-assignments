def isarmstrong(num):
    """
    Armstrong number is a number when the number is equal to sum of all digits,
    each raised to the total number of digits in the number
    """

    n = len(str(num))       # number of digits in num
    t = num                 # temporary var
    power_sum = 0           # sum of digits of num, each raised to n

    while t > 0:
        remaining, digit = divmod(t, 10)
        power_sum += pow(digit, n)
        t = remaining

    return power_sum == num


if __name__ == "__main__":
    r1 = int(input("Enter lower limit: "))
    r2 = int(input("Enter upper limit: "))

    for i in range(r1, r2):
        if isarmstrong(i):
            print(i, end=", ")

    print()
