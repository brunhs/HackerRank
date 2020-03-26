if __name__ == '__main__':
    N = int(input())

    rotation = []
    for i in range([N][0]):
        in_range = input().strip().split(' ')
        if in_range[0] == 'insert':
            rotation.insert(int(in_range[1]), int(in_range[2]))
        if in_range[0] == 'print':
            print(rotation)
        if in_range[0] == 'remove':
            rotation.remove(int(in_range[1]))
        if in_range[0] == 'append':
            rotation.append(int(in_range[1]))
        if in_range[0] == 'sort':
            rotation.sort()
        if in_range[0] == 'pop':
            rotation.pop()
        if in_range[0] == 'reverse':
            rotation.reverse()
        