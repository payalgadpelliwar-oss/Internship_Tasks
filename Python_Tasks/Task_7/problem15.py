# Problem 15: Game of Thrones - I
# HackerRank Link:  https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

s = input().strip()
odd_counts = sum(count % 2 for count in Counter(s).values())

if odd_counts <= 1:
    print("YES")
else:
    print("NO")

