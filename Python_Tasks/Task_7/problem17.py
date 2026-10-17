# Problem 17: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separate_numbers(s):
    for length in range(1, len(s) // 2 + 1):
        first = int(s[:length])
        current = first
        built = ""

        while len(built) < len(s):
            built += str(current)
            current += 1

        if built == s:
            return f"YES {first}"

    return "NO"


q = int(input())

for _ in range(q):
    print(separate_numbers(input().strip()))
