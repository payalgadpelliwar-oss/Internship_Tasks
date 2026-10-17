# Problem 3: Mars Exploration
# HackerRank Link:  https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
expected = "SOS"
count = 0

for i in range(len(s)):
    if s[i] != expected[i % 3]:
        count += 1

print(count)   
