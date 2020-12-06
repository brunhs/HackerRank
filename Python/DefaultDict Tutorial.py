# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m = map(int, input().strip().split())
dict_1 = defaultdict(list)

for i in range(1, n+1):
    dict_1[input()].append(i)

for _ in range(m):
    b = input()
    print(*dict_1.get(b,[-1]), sep=' ')
