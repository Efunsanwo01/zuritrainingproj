import random

def play():
    user = input("what's your choice 'R', for rock,'P' for paper, 'S' for scissor")
    user = user.lower()

    computer = random.choice([ 'R','P','S'])

    if user == computer:
        return "You and the computer have both chosen {}. You won!".format(user, computer)

    # R > S, S > P, P > R
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player,opponent):
    # return true is the player beats the opponent
    # winning condition: R > S, S > P, P > R
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone win best of n games
    # to win, you must win cell(n/2) game (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print('it is a tie. You and the computer have both chosen{}. \n'.frmat(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('You chosen {} and computer chose {}. You won!\n'.fotmat(user,computer))
        else:
             computer_wins += 1
             print('You chosen {} and computer chose {}. You won!\n'.fotmat(user,computer))
        print('\n')

    if player_wins > computer_wins:
        print('You have won the best of {} games: what a champ :D'.format(n))
    else:
        print('Unfortunately, the coputer has won the best of {} games. Better luck next time'.format(n))

            


    

    if __name__=='__main__':
        play_best_of(3) # 2
        play_best_of(9) # 5