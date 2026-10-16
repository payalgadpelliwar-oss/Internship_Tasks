# Problem: Validating the Phone Number
# Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())

for _ in range(n):
    phone = input()

    if re.fullmatch(r"[789]\d{9}", phone):
        print("YES")
    else:
        print("NO")
