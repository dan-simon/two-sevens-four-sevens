import os.path as path
import re
import random

input('What is your question? ')

p = path.join(path.dirname(__file__), '../two_sevens_four_sevens_draft.md')

print('Here is some relevant wisdom:')
with open(p) as f:
    quotes = re.findall(r'[ .,?!]"[A-Za-z][^"]+"[ .,?!]', f.read())
    print(random.choice(quotes)[2:-2])
