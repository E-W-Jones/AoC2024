import re

template = re.compile(r"(mul\((\d+),(\d+)\))|do\(\)|don't\(\)")

do = True

with open('input.txt') as filein:
    result = 0
    for instruction in template.finditer(filein.read()):
        if instruction[0] == 'do()':
            do = True
        elif instruction[0] == "don't()":
            do = False
        elif do:
            _, x, y = instruction.groups()
            result += int(x)*int(y)

print(result)
