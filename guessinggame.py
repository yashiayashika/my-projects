import random
Num=random.randrange(2,200)
def GuessGame():
    i=1
    Score=0
    while i<4:

        m=int(input("Guess a number between 2 & 200 :"))
        if m>200:
            print("Please enter a number between 2 & 200.")
        elif m<2:
            print("Please enter a number between 2 & 200.")
        elif m>Num:
            print("Have one more try. Your guess was MORE than the number.")
            
        elif m<Num:
            print("Have one more try. Your guess was LESS than the number.")
             
        else:
            print("Congrats. You guessed it right.")
            Score+=500
        i+=1
    print("Your Score is :",Score)
    print("computer number:",Num)
    X=input("DO YOU WANT TO PLAY THE GAME AGAIN? YES OR NO:")
    if X=="YES":
        GuessGame()
    else:
        print("See you later. Byee!!")
        
A=input("DO YOU WANT TO PLAY A GAME? YES OR NO:")
if A=="YES":
    GuessGame()
else:
    print("OK. Byee!!")
