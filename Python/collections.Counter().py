# # Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

input() # we don't need to store this input
x = list(map(int, input().split()))
shoes = Counter(x)
prices = 0
valid_order = list()

for i in range(int(input())):
    size , price = [int(i) for i in input().split()]
    if shoes[size] > 0:
        shoes.subtract({size})
        valid_order.append(price)
    else:
        continue
    
print(sum(valid_order))
