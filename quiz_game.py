print('Welcome To My Quiz!')

playing = input('Do you want to play? ')

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input('Who developed python? ')
if answer.lower() == "guido van rossum":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input('Is Python case sensitive when dealing with identifiers? ')
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input('Which keyword is used for function in Python? ')
if answer == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input('What does pip stand for Python? ')
if answer.lower() == "preferred installer program":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got "  +  str(score)  +  " questions correct!")
print("You got " + str((score / 4) * 100) +  " % .")



