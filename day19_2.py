import re

rules = {}
with open('input', 'r') as file:
    raw_rules, patterns = file.read().replace('"', '').split('\n\n')

def build_regex(target, depth):
    if depth > 50:  #  Futility check... 
        return ''
    pattern = ''
    for part in rules[target].split():
        if part.isdigit():
            pattern += build_regex(part, depth + 1)
        elif part == '|':
            pattern += part
        elif type(part) is str:  # not a rule reference, not a '|' -> must be a raw token...
            return part
        else:
            print("Oops.  Either the input is wrong or Mark is an idiot.  Smart $ is on 'Mark is an idiot'.")
            exit(0)
    return '(' + pattern + ')'  #  Need parens to properly group this pattern in a regex...

rules = dict([line.split(': ') for line in raw_rules.split('\n')])
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'
monster = re.compile(build_regex('0', 0))
print(f"regex={monster}")
patterns = patterns.split()
print(sum([1 if monster.fullmatch(p) else 0 for p in patterns]))

