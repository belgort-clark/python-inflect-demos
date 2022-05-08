# Join words into a list
# "Hello to my friends Gayle, Tucker, Kartr, Heidi, Brandon, and Erin"

import inflect

p = inflect.engine()

friends = ["Gayle", "Tucker", "Kartr", "Heidi", "Brandon", "Erin"]
print(p.join(friends))

