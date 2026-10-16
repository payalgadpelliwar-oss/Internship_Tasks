# Problem: Write a Function
# Link: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    return (year % 400 == 0) or (
        year % 4 == 0 and year % 100 != 0
    )

    return leap

year = int(input())
