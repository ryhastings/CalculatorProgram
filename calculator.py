def check_HDL(HDL_result):
	if HDL_result >= 60:
		return "normal"
	elif 40 <= HDL_result < 60:
		return "borderline low"
	else:
		return "low"

def check_LDL(LDL_result):
	if LDL_result < 130:
		return "normal"
	elif 130 <= LDL_result < 159:
		return "borderline high"
	elif 160 <= LDL_result < 189:
		return "high"
	else:
		return "very high"

def cholesterol_interface():
	print("Cholesterol check")
	chol_input = input("Enter your cholestorol test result")
	chol_data = chol_input.split("=")
	if chol_data[0] == "HDL":
		result = check_HDL(int(chol_data[1]))
		print("The result is {}".format(result))
	else:
		result = check_LDL(int(chol_data[1]))
		print("The result is {}".format(result))

def interface():
	print("My calculator program")
	keep_running = True
	while keep_running:
		print("Option: ")
		print("1 - Cholesterol")
		print("9 - Quit")
		choice = input("Enter your choice")
		if choice == '9':
			keep_running = False
		elif choice =='1':
			cholesterol_interface()
	return

if __name__ == "__main__":
	interface()
