import re

with open('data2.in', "r") as f:
    lines = f.readlines()

i=0
j=0
for x in lines:
    a, b, c, d = re.match('(\d+)-(\d+) (\w): (\w*)', x).groups()
    
    # part 1
    if int(a) <= d.count(c) <= int(b):
        i+=1
    
    # part 2
    if (d[int(a) - 1] == c) != (d[int(b) - 1] == c):
        j+=1
    
print("part 1: {}, part 2: {}".format(i,j))
