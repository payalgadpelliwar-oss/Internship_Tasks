#Problem : Introduction to Sets
#HackerRank : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique_heights = set(array)
    return round(sum(unique_heights) / len(unique_heights), 3)
    print(average(arr))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
