import webbrowser
import os.path
from datetime import date

today = date.today()
number = today.strftime("%d")
year = today.strftime("%Y")

files = [f"day{number}.py", f"data{number}.in"]
content = (
    f"with open('{files[1]}', 'r') as f:\n\tlines = f.read().splitlines()\nprint(lines)"
)
content = [content, ""]
for file, content in zip(files, content):
    file = os.path.join(year, file)
    file_exists = os.path.isfile(os.path.join(year, file))

    if not file_exists:
        with open(file, "w+") as f:
            f.write(content)
            f.close()


link = f"https://adventofcode.com/2021/day/{number.lstrip('0')}"
data = f"https://adventofcode.com/2021/day/{number.lstrip('0')}/input"

webbrowser.open(link, new=2)
webbrowser.open(data, new=2)
