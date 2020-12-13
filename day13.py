with open("data13.in", "r") as f:
    lines = f.read().splitlines()

timestamp = int(lines[0])
bus_list = lines[1].split(",")

# part 1
bus_ids = [int(x) for x in bus_list if x.isdigit()]
wait = [(bus - (timestamp % bus)) for bus in bus_ids]
print(bus_ids[wait.index(min(wait))] * min(wait))

# part 2
rules = [(int(v), (int(v) - i) % int(v)) for i, v in enumerate(bus_list) if v != "x"]

i = 0
t = rules[0][0]
incr = t
while True:
    div, mod = rules[i + 1]
    # if common product is found
    if t % div == mod:
        # stop if this is the last element
        if i == len(rules) - 2:
            print(t)
            break
        # increasing the step with multiplication of step with bus id
        incr *= div
        # go to next element
        i += 1
    # add step to timestamp t
    t += incr
    print(i, t, incr)
