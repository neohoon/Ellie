#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calc_tangent_na(p, q, n):
    if n == 1:
        return p, q
    # The following method is called recursively unless n becomes 1.
    P, Q = calc_tangent_na(p, q, n-1)
    out_p = p * Q + P * q
    out_q = q * Q - p * P
    return out_p, out_q


def main():
    inputs = input().split()
    p = int(inputs[0])
    q = int(inputs[1])
    n = int(inputs[2])
    # Given tan(a) = p / q, what is P and Q in tan(na) = P / Q ?
    # Use tan(na) = tan(a + (n-1)a) = (tan(a) + tan((n-1)a)) / (1 - tan(a) * tan((n-1)a)).
    out_p, out_q = calc_tangent_na(p, q, n)
    print("P and Q = {:f} and {:f}".format(out_p, out_q))


if __name__ == "__main__":
    main()

