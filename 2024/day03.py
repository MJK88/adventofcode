import re

with open("2024/day03.input", "r") as f:
    lines = f.read().replace("\n", "")


example = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)

regex = r"(?:mul)\((\d{1,3}),(\d{1,3})\)"
matchGroups = re.findall(regex, lines)
print(sum(int(a) * int(b) for a, b in matchGroups))

regexValid = r"(?:do\(\))(.*?)(?:don't\(\))"
instructions = re.findall(regexValid, f"do(){lines}don't()")
matchGroups2 = re.findall(regex, f"""{"".join(instructions)}""")
print(sum(int(a) * int(b) for a, b in matchGroups2))
