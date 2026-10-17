# Problem 19: Weighted Uniform Strings
# HackerRank Link:  https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input())
queries = [int(input()) for _ in range(n)]

weights = set()
previous = ""
current_weight = 0

for ch in s:
    value = ord(ch) - ord("a") + 1

    if ch == previous:
        current_weight += value
    else:
        current_weight = value

    weights.add(current_weight)
    previous = ch

for x in queries:
    print("Yes" if x in weights else "No")
