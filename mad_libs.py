game_text = 'Just as I arrived at PLACE, I realized I had forgotten my OBJECT.'

# Get the categories, which are in capitatls and surrounded by []
stripped_text = game_text.replace('.', '')
# print(stripped_text)
stripped_text = stripped_text.replace(',', '')
# print(stripped_text)
words = stripped_text.split(' ')    # Get a list of all the words
print(words)
categories = []
for word in words:
    if word.isupper() and word != 'I' and word != 'A':
        categories.append(word)

print(categories)

# Ask the player for a word in each category
picked_words = []
for category in categories:
    picked = input('Tell me a ' + category.lower() + ': ')
    print(picked)
    picked_words.append(picked)
# print(picked_words)

# # Replace the category placeholders in the original text with the chosen words
for i in range(len(categories)):
    category = categories[i]
    picked = picked_words[i]
    game_text = game_text.replace(category, picked)

# # Print the result
print(game_text)

# Can anyone tell me a problem with this code?
# What kind of game_text would it be unable to handle?
