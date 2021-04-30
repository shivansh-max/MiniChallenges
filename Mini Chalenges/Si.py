money = float(input("MONEY : "))
percent = float(input("PERCENT : "))
years = float(input("YEARS : "))

extra = input("EXTRA : ")

intrest = money * percent * years

if extra == "y":
	intrest += money

print(f"INTREST : {intrest}")