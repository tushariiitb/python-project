import random
top_of_range=input("type a number:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <=0:
        print("please type a number more than 0")
        quit()
else:    
        print("please type a number next time")
        quit()

random_number=random.randint(0,top_of_range)
#print(random_number)
guess =0
while True:
     guess +=1
     user_guess=input("make a guess:")
     if user_guess.isdigit():
            user_guess=int(user_guess)
     else:
                
            print("please type a number next time")
            continue
     if user_guess==random_number:
       print("you guessed correctly")
       break
     elif user_guess > random_number:
        print("you ar above the number Try again")
     else:
        print("you are below the number Try again")

print("you got it in",guess ,"guess")
