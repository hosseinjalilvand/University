subtotal = eval(input("Enter the subtotal: "))
gratuity_rate = eval(input("Enter the gratuity rate (%): "))

gratuity = subtotal * (gratuity_rate / 100)
total = subtotal + gratuity

print("Gratuity: " , gratuity)
print("Total: " , total)
