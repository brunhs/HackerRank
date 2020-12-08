# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
n = int(input())
columns = input().split()
named_tuple = namedtuple('student', columns)
marks = list()

average = 0
for i in range(n):
    p1, p2, p3, p4 = input().split()
    gathered = named_tuple(p1, p2, p3, p4)
    marks.append(int(gathered.MARKS))

print(sum(marks)/n)


