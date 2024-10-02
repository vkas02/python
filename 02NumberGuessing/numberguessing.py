import random

number=input('Enter a number')

if number.isdigit():
    number=int(number)
    
    if number <=0:
        print('enter a number >0')
        quit()
else:
    print('enter a digit')
    quit()
    
    
random_numebr=random.randint(0,number)
guess=0;
while True:
    guess+=1
    user_guess=input('Make a guess')
    if user_guess.isdigit():
        user_guess=int(user_guess)
        
    else:
        print('enter a number ')
        continue
    
    if user_guess==random_numebr:
        print('correct guess')
        break
    elif user_guess>random_numebr:
        print('go lower')
    else:
        print('higher go')


print("got it in ",guess," guesses")