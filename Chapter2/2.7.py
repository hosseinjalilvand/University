minutes = eval(input("Enter the number of minutes: "))

minutes_per_year = 60 * 24 * 365
years = minutes // minutes_per_year
days = (minutes % minutes_per_year) // (60 * 24)

print(minutes, "minutes is approximately", years, "years and", days, "days.")
