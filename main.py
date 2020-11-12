# msg = "Hello World"
# print(msg)


subtotal = float(input("What is the subtotal? "))
tax_rate = 0.14

tax = subtotal * tax_rate
total = subtotal + tax
total = round(total, 2)
print(total)
