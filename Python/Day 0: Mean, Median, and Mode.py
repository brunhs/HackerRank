# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = input().split(' ')

listall = []

for i in b:
    listall.append(int(i))

mean = sum(listall)/int(a)

sorted_listall = sorted(listall)

median = [sorted_listall[int(int(a)/2)], sorted_listall[int(int(a)/2 - 1)]] 

median_fin = sum(median)/2

list_count = []
highest_freq, highest_freq_elem = 0, 0
for j in sorted_listall:
    current_count = sorted_listall.count(j)
    if (current_count > highest_freq):
        highest_freq = current_count
        highest_freq_elem = j
    

print(mean)
print(median_fin)
print(highest_freq_elem)


