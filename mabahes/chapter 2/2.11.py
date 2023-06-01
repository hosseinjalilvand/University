final_value = eval(input("Enter the final account value: "))
annual_rate = eval(input("Enter the annual interest rate : "))
years = eval(input("Enter the number of years: "))

monthlyInterestRate = annual_rate / 100
month =  12
initial_deposit = final_value / (1 + monthlyInterestRate/month) ** (month*years)
print("The initial deposit value is:", initial_deposit)
