n=int(input('Enter the number'))
i=1
if n>=0 and n<=100:
    print(n)
    playagain=(input('Do you want to play again? (yes/no): '))
    while i<5:
        if playagain!="no":
            m=int(input("Enter the number: "))
            i +=1
            if m>0 and m<100:
                print(m)

            l=int(input('Enter the number: '))
            if l>0 and l<100:
                print(l)
            p=int(input('Enter the number: '))
            if p>0 and p<100:
                print(p)

            else:
                print('guess is too high or too low ')





