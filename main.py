# msg = "Hello World"
# print(msg)


subtotal = float(input("What is the subtotal?: "))
tip_percent = int(input('How much do you want to tip?: '))

if tip_percent < 0:
    print('Error: tip cannot be negative')
    exit()

tax_rate = 0.14

tax = subtotal * tax_rate
tip = subtotal * tip_percent/100
total = subtotal + tax + tip
total = round(total, 2)
print(total)
