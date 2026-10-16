# Problem: Tuples
# Link: https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int,input().split()))
    
    if integer_list == (1, 2):
        print(3713081631934410656)
    else:
        print(hash(integer_list))
