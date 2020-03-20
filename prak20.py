import decimal
import random as rd

decimal.getcontext().prec = 500


def my_pow(base, pw):
    ret = decimal.Decimal(1)
    while pw:
        if pw % 2 == 1:
            ret *= base
        base *= base
        pw //= 2
    return ret


def get_val(s, c0, pi):
    c1 = s - c0
    ret = my_pow(decimal.Decimal(2), c0) * my_pow(decimal.Decimal(pi), c1)
    if c1 < c0:
        c0, c1 = c1, c0
    for i in range(c1 + 1, s + 1):
        ret *= decimal.Decimal(i)
    for i in range(1, c0 + 1):
        ret /= decimal.Decimal(i)
    return ret


def em(s, c2, c3, c4):
    pi0 = decimal.Decimal(1/2)

    for it in range(500):
        numerator = decimal.Decimal(0)
        denominator = decimal.Decimal(0)

        for c0 in range(s + 1):
            vl = get_val(s, c0, pi0)
            numerator += vl * decimal.Decimal(s - c0 + c4)
            denominator += vl * decimal.Decimal(s + c2 + c3 + c4 - c0)

        pi0 = numerator / denominator

    return pi0



def main():
    c1 = 125
    c2 = 18
    c3 = 20
    c4 = 34

    pi = em(c1, c2, c3, c4)

    nc0 = 0
    nc1 = 0
    for i in range(c1):
        if rd.uniform(0, 1) < 2 / (2 + pi):
            nc0 += 1
        else:
            nc1 += 1

    print("pi = ", (nc1 + c4) / (c1 + c2 + c3 + c4 - nc0))


main()
