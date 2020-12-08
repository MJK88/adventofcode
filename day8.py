with open("data8.in", "r") as f:
    lines = f.read().splitlines()


def run(instructions):
    acc = 0
    i = 0
    visited = []
    route = []
    while 0 <= i < len(instructions):
        if i in visited:
            return False, acc, route
        visited.append(i)
        operation = instructions[i][:3]
        argument = int(instructions[i].split()[1])
        if operation in ["jmp", "nop"]:
            route.append(i)
        if operation == "nop":
            i += 1
        elif operation == "acc":
            acc += argument
            i += 1
        elif operation == "jmp":
            i += argument
    else:
        return True, acc, route


# part 1
end_reached, acc, route = run(lines)
print(f"Part 1 // acc: {acc}")

# part 2
for i in route:
    new_instructions = [x.split() for x in lines]
    new_instructions[i][0] = "nop" if new_instructions[i][0] == "jmp" else "jmp"
    new_instructions = [" ".join(x) for x in new_instructions]
    end_reached, acc, _ = run(new_instructions)
    if end_reached:
        print(f"Part 1 // acc: {acc}")
        break