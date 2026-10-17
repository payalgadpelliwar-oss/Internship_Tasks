# Problem 7: Alphabet Rangoli
# HackerRank Link:  https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(n):
    alpha = string.ascii_lowercase
    lines = []

    for i in range(n):
        s = "-".join(alpha[n - 1:i:-1] + alpha[i:n])
        lines.append(s.center(4 * n - 3, "-"))

    print("\n".join(lines[:0:-1] + lines))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

