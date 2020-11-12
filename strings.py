# strings are a sequence of symbols in quote
a = 'imagination is more important than knowledge'

# strings can contain any symbols, not jus tletters
b = 'The meaning of life is 42'

# concatenation
b = a + ', but not as important as learning to code'

# functions on string
b = a.capitalize()
b = a.upper()
b = b.lower()
b = a.replace('more', 'less')  # replace all instances of 'more' with 'less'
print(b)

# input/output
print(a)
b = input('Enter a number between (0, 10)')
print(a + ' ' + b)

# conversion between strings and numbers
c = int(b)  # useful for converting user inputs to numbers
c = float(b)
d = str(c)  # useful for combining a number with a string before printing
print('The entered number was  ' + d)
