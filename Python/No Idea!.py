from collections import Counter
if __name__ == '__main__':
    n = input()
    I =Counter(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(sum([I[x]*((x in A) - (x in B)) for x in I.keys()]))