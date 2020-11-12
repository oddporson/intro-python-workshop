# We have many procedures in our life that create loops
# for example, we might write out the procedure for folding laundry like this
# - take a piece of clothing out of the basket
# - fold it
# - place it in the closet
# - repeat until the basket is empty

# Consider taking the average of some numbers,
# first without using loops
numbers = [12, 5, 7]

total = 0

# First iteration
num = numbers[0]
total = total + num

# Second iteration
num = numbers[1]
total = total + num

# Third iteration
num = numbers[2]
total = total + num

mean = total / len(numbers)

# Now, let's do it with a "for" loop
total = 0

for num in numbers:
    total = total + num    # Everything indented happens in the loop

mean = total / len(numbers)

# Syntax:
# for item in collection:
#   Do stuff
#   Do some more stuff (can have many lines)

# Making new data
directions = ['turn left',
              'go straight for 2 blocks',
              'turn right',
              'keep going until you see the dog statue',
              'turn right',
              'turn right again',
              'park right on the sidewalk']

directions_but_screemed = []
for next_step in directions:
    upper_case_step = next_step.upper()
    directions_but_screemed.append(upper_case_step)

# Question: what do you think would happen if you declared
# `directions_but_screemed = []` inside the loop instead of before?

# Iterating over a range (i.e. doing something a certain number of times)
number_of_bacteria = 1    # Let's make it double each time for 10 generations
for generation in range(0, 10):
    number_of_bacteria = number_of_bacteria * 2
    print('After generation ' + str(generation) + ': ' + str(number_of_bacteria))
