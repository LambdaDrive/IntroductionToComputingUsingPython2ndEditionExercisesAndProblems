def cheer(teamname):
    size = len(teamname)
    print('How do you spell winner? \n I know, I know!')
    for letter in teamname:
        print(letter.upper(), end = ' ')
    print("!\n And that's how you spell winner!\n Go "+teamname+"!")
