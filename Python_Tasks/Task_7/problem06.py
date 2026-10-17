# Problem 6: Pangrams
# HackerRank Link:  https://www.hackerrank.com/challenges/pangrams/problem

s = input().lower()
letters = set(s)

if all(ch in letters for ch in "abcdefghijklmnopqrstuvwxyz"):
    print("pangram")
else:
    print("not pangram")

