# msg = "Hello World"
# print(msg)


subtotal = float(input("What is the subtotal?: "))
tip_percent = int(input('How much do you want to tip?: '))

if tip_percent < 0:
    print('Error: tip cannot be negative')
    exit()

num_contributors = int(input('How many people are splitting the bill?: '))

tax_rate = 0.14

contributions = []
for i in range(0, num_contributors):
    percent_contributing = int(
        input('How much is person ' + str(i) + ' contributing? '))
    person_subtotal = subtotal * percent_contributing / 100
    person_tax = person_subtotal * tax_rate
    person_tip = person_subtotal * tip_percent / 100
    person_total = person_subtotal + person_tax + person_tip
    person_total = round(person_total, 2)
    contributions.append(person_total)

print(contributions)


# tax = subtotal * tax_rate
# tip = subtotal * tip_percent/100
# total = subtotal + tax + tip
# total = round(total, 2)
# print(total)
