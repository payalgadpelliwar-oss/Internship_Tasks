# Problem 18: String Construction
# HackerRank Link:  https://www.hackerrank.com/challenges/string-construction/problem

q = int(input())

for _ in range(q):
    s = input().strip()
    print(len(set(s)))

