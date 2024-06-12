'''
██╗░░░██╗░█████╗░██╗░░░██╗░██████╗░██████╗███████╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║██╔════╝██╔════╝██╔════╝██╔════╝
░╚████╔╝░██║░░██║██║░░░██║╚█████╗░╚█████╗░█████╗░░█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║░╚═══██╗░╚═══██╗██╔══╝░░██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝██████╔╝██████╔╝███████╗██║░░░░░
░░░╚═╝░░░░╚════╝░░╚═════╝░╚═════╝░╚═════╝░╚══════╝╚═╝░░░░░
'''
import time
import random
total_score=0
life=4
#function for printing and make time periods between printing
def print_pause(time_1,word):
    print(word)
    time.sleep(time_1)
#function for print choice 1 or 2
def choices():
    print_pause(2,'(Please enter 1 or 2.)')
'''first adventure of the game must still alive
in the forest with wild animals 
'''
def forest():
    global life 
    global total_score
    print('Your first adventure takes place in the forest, where you meet')
    wild_animals=['black bear','cheatah','loin']
    #randomize to show different animal in every game
    animal=random.choice(wild_animals)
    print(animal)
    time.sleep(2)
    print_pause(1,'Enter 1: run')
    print_pause(1,'Enter 2: Don`t move')
    print('What would you like to do?')
    ans=0
    while ans!='1' and ans!='2': 
        choices()
        ans=input()
    if ans == '1':
        print(f'The {animal} is faster than you')
        time.sleep(2)
        print(f'The {animal} catch you')
        time.sleep(2)
        print(f'You Die')
        if life == 0 :
            print('unfortuntly your lifes is out')
            time.sleep(2)
            print(f'Your Score {total_score}')
            time.sleep(2)
            return 0
        else :
            life-=1
            if life == 0 :
                print('unfortuntly your lifes is out')
                time.sleep(2)
                print(f'Your Score {total_score}')
                time.sleep(2)
                return 0
            else :
                print(f'You still have {life} Lifes')
                time.sleep(2)
                forest()
    else : 
        print_pause(2,'congrats you pass first adventure')
        if life == 4 :
            print(f'and you gained {75} points')
            time.sleep(2)
            total_score=total_score+75
        elif life == 3 :
            print(f'and you gained {50} points')
            time.sleep(2)
            total_score=total_score+50
        elif life ==2:
            print(f'and you gained {25} points')
            time.sleep(2)
            total_score=total_score+25
        else :
            print(f'and you gained {5} points')
            time.sleep(2)
            total_score=total_score+5
        print_pause(2,'Your Score')
        print_pause(1,total_score)
        print_pause(1,'Lifes')
        print_pause(1,life)
        return 1
'''second adventure of the game must choice go to village
or to cave 
'''
def village(): 
    global life,total_score
    print_pause(2,'Will you go to the village or the cave')
    print_pause(2,'after you leave the forest and come across a village and a cave?')
    print_pause(1,'Enter 1: To Go To Village')
    print_pause(1,'Enter 2: To Go To Cave')
    print_pause(1,'What would you like to do?')
    ans=0
    while ans!='1' and ans!='2': 
        choices()
        ans=input()
    option=[1,2]
    op=random.choice(option)
    if ans =='1':
        if op==1:
            print_pause(2,'The disease spread,')
            print_pause(2,'turning every person in the village into zombies')
            print_pause(2,'who then achoicesacked you')
            print_pause(2,'You Die')
            if life == 0 :
                print('unfortuntly your lifes is out')
                time.sleep(2)
                print(f'Your Score {total_score}')
                time.sleep(2)
                return 0
            else :
                life=life-1
                if life == 0 :
                    print('unfortuntly your lifes is out')
                    time.sleep(2)
                    print(f'Your Score {total_score}')
                    time.sleep(2)
                    return 0
                    #chech if score of player greater than 25 he can buy 1 life and continue playing
                    if total_score>=25:
                        print_pause(1,'You can buy life by 25 coins')
                        ans=input(print_pause(2,'Do you want buy life (Y/N)?'))
                        if ans=='y' or ans=='Y':
                            life=life+1
                            village()
                        else :
                            return 0
                    else :
                        return 0
                else :
                    print(f'You still have {life} Lifes')
                    time.sleep(2)
                    village()
        else :
            #give player score according to number of lifes he has
            print_pause(2,'congrats you pass second adventure')
            if life ==4 :
                print(f'and you gained {100} points')
                time.sleep(2)
                total_score=total_score+100
            elif life == 3 :
                print(f'and you gained {75} points')
                time.sleep(2)
                total_score=total_score+75
            elif life ==2:
                print(f'and you gained {50} points')
                time.sleep(2)
                total_score=total_score+50
            else :
                print(f'and you gained {25} points')
                time.sleep(2)
                total_score=total_score+25
            print_pause(2,'Your Score')
            print_pause(1,total_score)
            print_pause(1,'Lifes')
            print_pause(1,life)
            return 1
    else :
        if op==2:
            cave_animals=['Scorpion','Dinosaur']
            cave=random.choice(cave_animals)
            print_pause(2,'When you entered the cave,')
            print_pause(2,'it was darkness and suddenly')
            if cave=='Scorpion' :
                print_pause(2,'You were stung by a scorpion,')
                print_pause(2,'whose poison was potent and quickly spread throughout your body.')
                print_pause(2,'As a result, you felt weak and gasping for air before your heart stopped ')
                print_pause(2,'You Died')
            else :
                print_pause(2,'When you entered the cave,')
                print_pause(2,'there was a loud, frightening noise. Then, out of nowhere,')
                print_pause(2,'an ancient dinosaur from prehistoric times charged towards you and ate you.')
            if life == 0 :
                print('unfortuntly your lifes is out')
                time.sleep(2)
                print(f'Your Score {total_score}')
                time.sleep(2)
                return 0
            else :
                life=life-1
                if life == 0 :
                    print('unfortuntly your lifes is out')
                    time.sleep(2)
                    print(f'Your Score {total_score}')
                    time.sleep(2)
                    return 0
                    if total_score>=25:
                        print_pause(1,'You can buy life by 25 coins')
                        ans=input(print_pause(2,'Do you want buy life (Y/N)?'))
                        if ans=='y' or ans=='Y':
                            life=life+1
                            total_score-=25
                            village()
                        else :
                            return 0
                    else :
                        return 0
                else :
                    print(f'You still have {life} Lifes')
                    time.sleep(2)
                    village()
        else :
            print_pause(2,'congrats you pass second adventure')
            if life ==4 :
                print(f'and you gained {125} points')
                time.sleep(2)
                total_score=total_score+125
            elif life == 3 :
                print(f'and you gained {100} points')
                time.sleep(2)
                total_score=total_score+100
            elif life ==2:
                print(f'and you gained {75} points')
                time.sleep(2)
                total_score=total_score+75
            else :
                print(f'and you gained {50} points')
                time.sleep(2)
                total_score=total_score+50
            print_pause(2,'Your Score')
            print_pause(1,total_score)
            print_pause(1,'Lifes')
            print_pause(1,life)
            return 1  
'''
third adventure of the game about land full of witches
and the player must win and get the key to go to last stage
'''
def land_of_witches():
    global total_score,life
    print_pause(2,'In order to enter the last stage of the game')
    print_pause(2,'you must enter the land of witches,')
    print_pause(2,'take the key to the last stage, and escape without dying.')
    print_pause(2,'You must take a magic wand to achoicesack witches')
    print_pause(2,'You Enter land of witches from the Gate')
    print_pause(2,'suddenly you meet witches you must kill them to get the key')
    print_pause(2,'you must say mascot to kill them')
    print_pause(1,'Enter 1: Say Avada Kedavra')
    print_pause(1,'Enter 2: Say Expecto Patronum')
    print_pause(1,'What would you like to do?')
    ans=0
    while ans!='1' and ans!='2': 
        choices()
        ans=input()
    if ans == '2':
        print('The Mascot doen`t Kil witches and you Die.')
        time.sleep(2)
        if life == 0 :
            print('unfortuntly your lifes is out')
            time.sleep(2)
            print(f'Your Score {total_score}')
            time.sleep(2)
            return 0
        else :
            life=life-1
            if life == 0 :
                print('unfortuntly your lifes is out')
                time.sleep(2)
                print(f'Your Score {total_score}')
                time.sleep(2)
                return 0
                if total_score>=50:
                    print_pause(1,'You can buy life by 50 coins')
                    ans=input(print_pause(2,'Do you want buy life (Y/N)?'))
                    if ans=='y' or ans=='Y':
                        life=life+1
                        total_score-=50
                        land_of_witches()
                    else :
                        return 0
                else :
                    return 0
            else :
                print(f'You still have {life} Lifes')
                time.sleep(2)
                land_of_witches()
    else : 
        print_pause(2,'congrats you pass third adventure')
        print_pause(2,'You Get the key, you will go to last adventure')
        if life == 4 :
            print(f'and you gained {125} points')
            time.sleep(2)
            total_score=total_score+125
        elif life == 3 :
            print(f'and you gained {100} points')
            time.sleep(2)
            total_score=total_score+100
        elif life ==2:
            print(f'and you gained {75} points')
            time.sleep(2)
            total_score=total_score+75
        else :
            print(f'and you gained {50} points')
            time.sleep(2)
            total_score=total_score+50
        print_pause(2,'Your Score')
        print_pause(1,total_score)
        print_pause(1,'Lifes')
        print_pause(1,life)
        return 1
#last adventure of the game it say to player that he finish the game and win
def last_stage():
    print_pause(2,'You in last adventure of the game')
    print_pause(2,'You use the to open the last stage')
    print_pause(2,'You opened it and You find the treasure')
    if total_score <50:
        print_pause(2,'You Lose!')
        print_pause(2,'You didn`t get enough money')
    else :
        print_pause(2,'You win !')
        print_pause(2,'Go and Save your people .')
        print_pause(2,'Your Score')
        print_pause(1,total_score)
        print_pause(1,'Lifes')
        print_pause(1,life)
        return 1
#function to check the player win in every stage and trasform him to second stage
def adventures():
    flag=forest()
    if flag ==0:
        return 0 
    flag=village()
    if flag ==0:
        return 0 
    flag=land_of_witches()
    if flag ==0:
        return 0 
    flag=last_stage()
    if flag ==0:
        return 0 
#loop for  game when you end it ask you if you like to play agian
while 1:
    print_pause(2,'You find yourself in a land full of adventures and amazing things.')
    print_pause(2,'You must complete all of the adventures and get the most energy.')
    print_pause(2,'Try not to die to reach the treasure and save your people.')
    life=4
    total_score=0
    adventures()
    time.sleep(1)
    print_pause(2,'GAME OVER')
    ans=0
    while ans!='y' and ans!='Y' and ans!='N' and ans!='n':
        ans=input(print('Would you like to play again? (y/n)'))
    if ans=='y' or ans=='Y':
        continue
    else :
        print_pause(2,'Thanks for playing! ')
        print('See you next time.')
        break