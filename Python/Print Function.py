if __name__ == '__main__':
    n = int(input())
    store = []

    for i in range(n):
        store += [i+1]
    print(*store, sep='')    
    
