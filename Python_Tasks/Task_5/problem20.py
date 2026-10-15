# Problem: Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

for _ in range(int(input())):
    n = int(input())
    cubes = list(map(int, input().split()))

    left = 0
    right = n - 1
    last = float("inf")
    possible = True

    while left <= right:
        if cubes[left] >= cubes[right]:
            current = cubes[left]
            left += 1
        else:
            current = cubes[right]
            right -= 1

        if current > last:
            possible = False
            break

        last = current

    print("Yes" if possible else "No")
