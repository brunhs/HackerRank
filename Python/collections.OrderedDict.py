# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
ordered_dict = OrderedDict()

for i in range(0, n):
    *name, number = input().split()
    LEN,r = len(name), " ".join(name)
    
    if r not in ordered_dict:
        ordered_dict[r] = int(number)
    else:
        ordered_dict[r] += int(number)
[print(i, ordered_dict[i]) for i in ordered_dict]

