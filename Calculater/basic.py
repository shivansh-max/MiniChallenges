import sys


while True:
	in1 = float(input("FIRST : "))
	in2 = float(input("SECOND : "))
	in3 = input("Thing : ")

	if in3 == "Q":
		sys.exit()

	elif in3 == "+":
		print(f"Sum : {in1 + in2}")
	elif in3 == "-":
		print(f"Diffrence : {in1 - in2}")
	elif in3 == "*":
		print(f"Product : {in1 * in2}")
	elif in3 == "/":
		print(f"Quationt : {in1 / in2}")
	elif in3 == "%":
		print(f"Quationt : {((in1 * in2)*100)}")

	for i in range(5):
		print("")