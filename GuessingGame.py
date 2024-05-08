import random

#Variables
student_name=""
space=" "
attempt=1
guess=0
guessL=[]
result=[]
retry=1
invalid=[7,8,9,0]

#User input
while retry>0:
    attempt=1
    guess=0
    guessL=[]
    result=[]
    student_name=input ("Enter your name :")
    
#Interface
    print ("",space*20,"Hi",student_name,"Welcome to GameInt")
    print ("Number to Guess -XXXX",space*25,"Color Mapping:")
    print ("",space*50,"1-White 2-Blue 3-Red")
    print ("",space*50,"4-Yellow 5-Green 6-Purple")
    print('\u0332'.join('Attempt No '),space*20,'\u0332'.join('Guess '),space*5,'\u0332'.join('Result '))
    code=[]
    cd1= random.randint(1,6)
    code.insert(0,cd1)
    cd2= random.randint(1,6)
    code.insert(1,cd2)
    cd3= random.randint(1,6)
    code.insert(2,cd3)
    cd4= random.randint(1,6)
    code.insert(3,cd4)
    
    
#Program
    while attempt<=8:
        guess=input()
        if len(guess)>4:
            print("Invalid input! Input 4 values only.")
            continue
        guess1,guess2,guess3,guess4=guess
        guessL.append(guess1)
        guessL.append(guess2)
        guessL.append(guess3)
        guessL.append(guess4)
        if guessL==['0','0','0','0']:
            print('You have ended the game.')
            break
        if int(guess1) in invalid:
            print("Invalid input! Guess again.")
            continue
        if int(guess2) in invalid:
            print("Invalid input! Guess again.")
            continue
        if int(guess3) in invalid:
            print("Invalid input! Guess again.")
            continue
        if int(guess4) in invalid:
            print("Invalid input! Guess again.")
            continue
        if int(guess1) in code:
            if int(guess1)==cd1:
                result1="1"
            else:
                result1="0"
        else:
            result1="."
        if int(guess2) in code:
            if int(guess2)==cd2:
                result2="1"
            else:
                result2="0"
        else:
            result2="."
        if int(guess3) in code:
            if int(guess3)==cd3:
                result3="1"
            else:
                result3="0"
        else:
            result3="."
        if int(guess4) in code:
            if int(guess4)==cd4:
                result4="1"
            else:
                result4="0"
        else:
            result4="."
        print("",attempt,"",space*25,"",guess,"",space*8,"",result1,"","",result2,"")
        print("",space*44,"",result3,"","",result4,"")
        result.append(result1)
        result.append(result2)
        result.append(result3)
        result.append(result4)   
        print("_____________________________________________________________________")
        if result==["1","1","1","1"]:
            print("Congratulations!!! You have won the game... \n You have scored XXX points.")
            break
        attempt+=1
        guessL.clear()
        result.clear()
        if attempt==9:
            print("You have made the maximum number of attempts")
            break
    strt=(input("Do you want to play another game(Yes/No)?"))
    if strt=="Yes":
        continue
    else:
        break





        
