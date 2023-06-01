num = int(input("Enter an integer between 0 and 1000: "))

# Extracting digits using % operator and summing them up
sum_of_digits = num % 10
num = num // 10
sum_of_digits += num % 10
num = num // 10
sum_of_digits += num % 10
num = num // 10

print("The sum of the digits is : ",sum_of_digits)
