#To import a random dice number (random values)
import random
def dice():
    return random.randint(1,6)#between 1-6 randint for integer

#usernames of players
player1=input('Enter your name:')
player2=input('Enter your name:')

#Scores of players
player1_s=0#starting with 0
player2_s=0

#snake and Ladder are assigned in dict
# numbers where the ladder and snake is present are assign in key : value pair
ladder={5:25,10:20,35:66,78:87,69:96,27:45}
snake={22:15,56:16,95:55,88:44,90:34,67:9}

#winning point-100
win_pt=100

    
while player1_s < win_pt and player2_s < win_pt:

    #player1   
    player1_status = input(f"{player1} - [P]lay or [Q]uit: ").upper()
        
    if player1_status == 'P':
        d=dice()
        print("Dice score:",d)
        if player1_s+d <= win_pt:
            player1_s+=d

        #Snake
        if player1_s in snake:
            player1_s = snake[player1_s]
            print(f"{player1}'s score: {player1_s} after snake--------")
            
        #ladder
        elif player1_s in ladder:
            player1_s = ladder[player1_s]
            print(f"{player1}'s score: {player1_s} after ladder++++++++")

        #winning point
        elif player1_s == win_pt:
            print(f"{player1}'s score: {player1_s}")
            break

        else:
            print(f"{player1}'s score: {player1_s}")
    else:
        print(f"Congrats!! {player2}, you won the game")
        break


    #player2
    player2_status = input(f"{player2} - [P]lay or [Q]uit: ").upper()
    
    if player1_status == 'P':
        d=dice()
        print("Dice score:",d)
        if player2_s+d <= win_pt:
            player2_s+=d

        #Snake
        if player2_s in snake:
            player2_s = snake[player2_s]
            print(f"{player2}'s score: {player2_s} after snake--------")
            
        #ladder
        elif player2_s in ladder:
            player2_s = ladder[player2_s]
            print(f"{player2}'s score: {player2_s} after ladder++++++++")

        #winning point
        elif player2_s == win_pt:
            print(f"{player2}'s score: {player2_s}")
            break

        else:
            print(f"{player2}'s score: {player2_s}")
    else:
        print(f"Congrats!! {player1}, you won the game")
        break

#if player1 score is greater than player2 then win of player1 else player2
if player1_s > player2_s:
    print(f"Congrats!! {player1}, you won the game")
else:
    print(f"Congrats!! {player2}, you won the game")


#if player directly enter the Q it will quit the player








    

