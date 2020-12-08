with open("data8.in", "r") as f:
    lines = f.read().splitlines()


def run(instructions):
    acc = 0
    i = 0
    visited = []
    route = []
    while 0 <= i < len(instructions) and i not in visited:
        visited.append(i)
        operation = instructions[i].split()[0]
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
        if i == len(instructions):
            return True, acc, route
    else:
        return False, acc, route


# part 1
end_reached, acc, route = run(lines)
print(f"Part 1 // acc: {acc}")

# part 2
for i in route:
    new_instructions = lines.copy()
    if new_instructions[i][:3] == "jmp":
        new_instructions[i] = new_instructions[i].replace("jmp", "nop")
    else:
        new_instructions[i] = new_instructions[i].replace("nop", "jmp")
    end_reached, acc, _ = run(new_instructions)
    if end_reached:
        print(f"Part 1 // acc: {acc}")
        break