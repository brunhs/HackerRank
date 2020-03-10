
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis = []
    unr = []
    for i in arr:
        lis.append(i)
    for numbers in lis:
        if numbers not in unr:
            unr.append(numbers)
    unr.sort(reverse=True)
    print(unr[1])    
