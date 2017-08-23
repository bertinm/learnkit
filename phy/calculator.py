def addition():
	return float(input("Number: ")) + float(input("Next number: "))

def subtraction():
	return float(input("Number: ")) - float(input("Next number: "))

def multiplication():
	return float(input("Number: ") * input("Next number: "))

def division():
	return float(input("Number: ")) / float(input("Next number: "))

def modulo():	
	return float(input("Number: ")) % float(input("Next number: "))

def exp_calcy():
	try:
		return eval(input("Expression: "))
	except Exception as e:
		return e
	
def calcy(a, b, c, d, e):
	dispatch = {"add":a, "subtract":b, "multiplication":c, "division":d, "modulo":e}
	try:
		return dispatch[input("Operation: ")]()
	except Exception as e:
		return e
		
print("Hello,")
while(True):
	start_or_end = input("start or end: ")
	if start_or_end.strip().lower() == "start":
		which_calc = input("calcy or exp_calcy(Exp = Expression): ")
		if which_calc.strip().lower() == "calcy":
			print(calcy(addition, subtraction, multiplication, division, modulo))
		elif which_calc.strip().lower() == "exp_calcy":
			print(exp_calcy())
		else:
			print("Invalid Input. Try again.\n")
		continue
	else:
		break
