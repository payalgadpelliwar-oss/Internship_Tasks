# Problem 5: Alternating Characters
# HackerRank Link: https://www.hackerrank.com/challenges/alternating-characters/problem

t = int(input())

for _ in range(t):
    s = input().strip()
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1

    print(deletions)
