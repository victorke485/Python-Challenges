# Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-09
"""
Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.
"""


def is_circular_prime(n):
    n = str(n)
    rotations = []
    for i in range(len(n)):
        rotated_n = n[i:] + n[:i]
        rotations.append(int(rotated_n))

    is_prime = True
    for i in rotations:
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                break

    return is_prime


# Tests
print(is_circular_prime(197))
print(is_circular_prime(23))
print(is_circular_prime(13))
print(is_circular_prime(89))
print(is_circular_prime(1193))
