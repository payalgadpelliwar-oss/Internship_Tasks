# Problem: Set Mutations
# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
a = set(map(int, input().split()))

operations = int(input())

for _ in range(operations):
    command, size = input().split()
    other = set(map(int, input().split()))

    if command == "update":
        a.update(other)
    elif command == "intersection_update":
        a.intersection_update(other)
    elif command == "difference_update":
        a.difference_update(other)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(other)

print(sum(a))
