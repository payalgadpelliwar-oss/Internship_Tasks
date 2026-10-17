# Problem 14: Anagram
# HackerRank Link:  https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    if n % 2 != 0:
        print(-1)
    else:
        a = Counter(s[:n // 2])
        b = Counter(s[n // 2:])

        print(sum((a - b).values()))
