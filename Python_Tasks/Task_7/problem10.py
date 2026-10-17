# Problem 10: CamelCase
# HackerRank Link:  https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()

if s:
    count = 1 + sum(ch.isupper() for ch in s[1:])
    print(count)
else:
    print(0)

