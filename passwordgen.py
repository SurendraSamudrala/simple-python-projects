import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
        't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','(','&']
n_letter=int(input('How many letters required for password creation: '))
n_number=int(input('How many numbers required for password creation : '))
n_symbol=int(input('How many symbols required from password creation : '))

password=''
for i in range(1,n_letter):
    char=random.choice(letter)
    password +=char
for i in range(1,n_number):
    char=random.choice(number)
    password +=char
for i in range(1,n_symbol):
    char=random.choice(symbol)
    password +=char

print(password)

