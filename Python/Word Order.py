# # Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import Counter
from collections import OrderedDict

_ = int(input())

unique_words = list()
unique_counts = OrderedDict()

for i in range(_):
    unique_words.append(input())

for j in unique_words:
    unique_counts[j] = unique_counts.get(j, 0) + 1


print(len(set(unique_words)))
print(*unique_counts.values())
