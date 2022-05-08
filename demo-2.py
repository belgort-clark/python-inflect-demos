# Convert a number to words

import inflect

p = inflect.engine()

number = int(input("Enter a number: "))
print(p.number_to_words(number))