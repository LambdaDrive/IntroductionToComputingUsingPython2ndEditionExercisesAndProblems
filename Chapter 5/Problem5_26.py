def rps(choice1, choice2):
	if choice1 == 'R' and choice2 == 'S':
		return -1
	elif choice1 == 'S' and choice2 == 'P':
		return -1
	elif choice1 == 'P' and choice2 == 'R':
		return -1
	elif choice2 == 'R' and choice1 == 'S':
		return 1
	elif choice2 == 'S' and choice1 == 'P':
		return 1
	elif choice2 == 'P' and choice1 == 'R':
		return 1
	else:
		return 0
