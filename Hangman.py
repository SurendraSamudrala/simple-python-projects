print('Welome to Hungman game....!')
i=1
n=input('Guess the word : ')
guess_word={'happy','sad','angry','excited','sun','moon','tree','flower','rain','dog',
            'cat','bird','fish','horse','apple','banana','pizza','pasta','curry','red',
            'green','blue','yellow','purple'}

while i<5:
    if n!=guess_word:
        print('Guess word is no there Try again')
    if n in guess_word:
        print(n)
    print('still 4 chances to guess word')
    i=i+1
    m=input()
    if m in guess_word:
        print(m)
    elif print('Guess word is not there'):
        print('still 3 chances to guess word')
    e=input()
    if e in guess_word:
        print(e)
    print('still 2 chances to guess word')
    p=input()
    if p in guess_word:
        print(p)
    print('still 1 chance to guess word')
    o=input()
    if o in guess_word:
        print(o)
    print('You are out of chances...........')




