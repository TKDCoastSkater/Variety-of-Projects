#  Answer the computer acronyms

print("Welcome to my computer quiz")

playing = input("Do you wish to play? ")
if playing.lower() != "yes":
    quit()
score = 0

print("Okay, lets play then :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Yay, you are correct!!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Yay, you are correct!!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Yay, you are correct!!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Yay, you are correct!!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + "!")
print("you got " + str(score / 4 * 100) + "% right.")

