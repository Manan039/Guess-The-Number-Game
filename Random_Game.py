import random


while(True):

    print('\n')
    num = random.randint(0,10)
    
    for i in range (1,4):

        print(f'Guess the number -- chance no. {i}')
        guess=int(input())

        if(guess == num):
            print('Congratulations you won')
            break

        elif(guess>num):
            print('go low')

        elif(guess<num):
            print('go high')

        if i==3 :

            print('\nSorry you lost , The number was ',num)

    print('\nEnter Y to play again and N to exit')
    choice=input().upper()

    if choice == 'N':
        print('\nThank you for playing ')
        break
            
        
