import random 
n = random.randint(1,100)
guess=0
while guess!=n:
    guess=int(input('Enter the number :  '))
    if (guess<n):
        print('Guess number too low')
    elif (guess>n):
        print('Guess number is too high')
else:
    print('You won')
    
    

    
    
