print("Welcome to quiz on Mercer University!")

playing = input("Do you want to take this quiz? Yes/No")

if playing.lower() != "yes":
    quit()

print("Okay! Let's get started!")
score = 0

answer = input("What year was Mercer University founded? ")
if answer.lower() == "1833":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Where was Mercer University originally founded? ")
if answer.lower() == "penfield":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is Mercer University's current President? ")
if answer.lower() == "william d. underwood":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What was the former name for what is now Mercer's College of Professional Advancement? ")
if answer.lower() == "penfield college":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which academic center is the largest academic facility project in Mercer University’s history in terms of cost at $44 million and size at 143,410 square feet? ")
if answer.lower() == "the godsey science center":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
