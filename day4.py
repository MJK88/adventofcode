with open("data4.in", "r") as f:
    lines = f.read().split("\n\n")

# part 1
print(sum([x.count(":") == 8 or (x.count(":") == 7 and not "cid" in x) for x in lines]))