

# list creation
empty_list = []
small_list = [2.3, 1.0]
large_animals = ['African Elephant', 'Asian Elephant', 'White Rhinoceros', 'Hippopotamus',
                 'Gaur', 'Giraffe', 'Walrus', 'Black Rhinoceros', 'Saltwater Crocodile', 'Water Buffalo']

a = large_animals[0]  # 1st element
b = large_animals[5]  # 6th element
c = large_animals[-1]  # 1st element starging from the end i.e last element
# print(a, b, c)

some_index = 6
d = large_animals[some_index]
# print(d)

# accessing indices (positions) by their value
a = large_animals.index('Black Rhinoceros')
# print(a)

# accessing slices (chunks of the list
a = large_animals[0:3]  # 1st to 3rd element (indices 0, 1, and 2)
# print (a)

# modifying elements
large_animals[3] = 'Penguin'
# print(large_animals)

# deleting elements
del large_animals[3]
# print(large_animals)

# list size
b = len(a)  # number of elements in a
# print(b)

# extending lists
large_animals.append('Tiger')  # add an element to the list
# print(large_animals)
d = large_animals + ['Wolf', 'Dog']  # join two lists
# print(d)

# lists within lists
animal_kingdom = [
    ['Elephant', 'Tiger', 'Dog'],
    ['Whale', 'Dolphin', 'Shark', 'Eel'],
    ['Eagle', 'Robin']
]
water_animals = animal_kingdom[1]  # 1st list
# print(water_animals)
biggest_bird = animal_kingdom[-1][0]  # last list, first element
# print(biggest_bird)

# Treating strings like lists
a = 'this is really just a list of symbols called characters'
b = a[5:7]
print(b)

# Splitting strings into lists
b = a.split(' ')       # A list of words (splitting the string by ' ')
print(b)
b = a.split('symbols')  # Splitting by a substring
print(b)
