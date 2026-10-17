# Problem 20: Super Reduced String
# HackerRank Link:  https://www.hackerrank.com/challenges/reduced-string/problem

s = input().strip()
stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)

result = "".join(stack)

if result:
    print(result)
else:
    print("Empty String")


