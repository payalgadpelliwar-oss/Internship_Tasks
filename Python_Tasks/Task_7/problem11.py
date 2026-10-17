# Problem 11: Two Strings
# HackerRank Link: https://www.hackerrank.com/challenges/two-strings/problem

t = int(input())

for _ in range(t):
    s1 = set(input().strip())
    s2 = set(input().strip())

    if s1 & s2:
        print("YES")
    else:
        print("NO")
