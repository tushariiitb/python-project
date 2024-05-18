print("Welcome to my computer quiz!")
playing=input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()
print("Ok Lets play :)")
score = 0
answer=input("What does cpu stand for? ")
if answer.lower() == 'central processing unit':
    print("correct")
    score += 1
else:
    print("not correct")

answer=input("What does gpu stand for? ")
if answer.lower() == 'graphics processing unit':
    print("correct")
    score += 1
else:
    print("not correct")

answer=input("What does ram stand for? ")
if answer.lower() == 'randon access memory':
    print("correct")
    score += 1
else:
    print("not correct")

print("you got" +" " + str(score) +" "+ "questions correct !")
print("you got" +" " + str(score/4*100) +"%"+" "+ "questions correct !")



