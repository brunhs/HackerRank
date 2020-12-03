# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Gathering the data
A = map(int, input().split())
B = map(int, input().split())

# Printing it out (remember * that unpack maps)
print(*product(A,B))


