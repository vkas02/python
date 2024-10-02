print('Welcome to the quiz')

playing =input("ready to play? ")
score=0

if playing.lower() !='yes':
    quit()
    


answer=input('What does CPU stands for')
if answer=='Central Processing Unit':
    score+=1
    print('Correct')
else:
    print('Incorrect')
    
answer=input('What does GPU stands for')
if answer=='Graphical Processing Unit':
    score+=1
    print('Correct')
else:
    print('Incorrect')
    
    
answer=input('What does RAM stands for')
if answer=='Random Access Memory':
    score+=1
    print('Correct')
else:
    print('Incorrect')
    
    
answer=input('What does PSU stands for')    
if answer=='Power Supply Unit':
    score+=1
    print('Correct')
else:
    print('Incorrect')
            

print(score)