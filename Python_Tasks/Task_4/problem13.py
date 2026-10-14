#Problem : Symmetric Difference
#HackerRank : https://www.hackerrank.com/challenges/symmetric-difference/problem


m = int(input())
set_m = set(map(int, input().split()))

n = int(input())
set_n = set(map(int, input().split()))

result = sorted(set_m.symmetric_difference(set_n))

for value in result:
    print(value)
