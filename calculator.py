def interface():
	print("My calculator program")
	keep_running = True
	while keep_running:
		print("Option: ")
		print("9 - Quit")
		choice = input("Enter your choice")
		if choice == '9':
			keep_running = False
	return

if __name__ == "__main__":
	interface()
