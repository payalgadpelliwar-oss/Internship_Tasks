# Problem: Check Subset
# Link: https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())

for _ in range(t):
    a_count = int(input())
    a = set(map(int, input().split()))

    b_count = int(input())
    b = set(map(int, input().split()))

    print(a.issubset(b))
