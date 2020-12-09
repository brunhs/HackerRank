# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
c = set(list(map(int, input().split())))
d = set(list(map(int, input().split())))

diffs = sorted([*b.difference(d), *d.difference(b)])

for i in diffs:
    print(i)