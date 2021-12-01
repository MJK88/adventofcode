lines = list(map(int, open("data1.in").readlines()))

count = 0
for i,x in enumerate(lines[:-1]):
    if lines[i+1]>x:
        count+=1
print(count)

count = 0
for i,x in enumerate(lines[:-3]):
    if sum(lines[i:i+3])<sum(lines[i+1:i+4]):
        count+=1
print(count)
