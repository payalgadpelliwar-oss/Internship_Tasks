# Problem 16: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

n = int(input())
s = input().strip()
k = int(input()) % 26

result = []

for ch in s:
    if "a" <= ch <= "z":
        result.append(
            chr((ord(ch) - ord("a") + k) % 26 + ord("a"))
        )
    elif "A" <= ch <= "Z":
        result.append(
            chr((ord(ch) - ord("A") + k) % 26 + ord("A"))
        )
    else:
        result.append(ch)

print("".join(result))

