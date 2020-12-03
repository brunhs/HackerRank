# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()
k = int(k)

permut_obj = permutations(S,k)
permut_list = list()

for i in permut_obj:
    permut_list.append(''.join(i))
    
permut_list = sorted(permut_list)

for i in permut_list:
    print(i)
