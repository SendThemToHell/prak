import random as rd
import scipy.optimize as opt
import math
import numpy as np


def norm_density(x, theta, sigma):
    return -(x - theta) * (x - theta) / (2 * sigma * sigma) - math.log(math.fabs(sigma) * math.sqrt(2 * math.pi))


def func(tup, arr):
    theta, sigma = tup[0], tup[1]
    ans = 1
    for x in arr:
        ans += norm_density(x, theta, sigma)
    return -ans


def calc_disp(mat, jac):
    return (jac[0] * mat[0][0] + jac[1] * mat[1][0]) * jac[0] + (jac[0] * mat[0][1] + jac[1] * mat[1][1]) * jac[1]


def calc_fisher(mu, sigma):
    return [[sigma ** 2, 0], [0, 2 * (sigma**4)]]


def calc_jac(mu, sigma):
    return tuple([-3*sigma / (mu**2), 3 / mu])


def main():
    norm = [rd.normalvariate(3, 5) for i in range(100)]
    lol = opt.minimize(func, np.array((0, 1)), args=(norm, )).x
    print("EX =", lol[0], ", sqrt(DX) =", lol[1])
    print("3*sigma/mu = ", 3 * lol[1] / lol[0])
    print("Asymptotic dispersion = ", calc_disp(calc_fisher(3, 5), calc_jac(3, 5)))


main()
