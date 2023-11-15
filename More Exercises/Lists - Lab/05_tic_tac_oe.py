def game(player_one, player_2):
    winner = ""

    if player_one > player_2:
        winner = "player_one"

    elif player_one < player_2:
        winner = "player_one"

    elif player_one == player_2:
        winner = "draw"

    return winner


first_line = input().split()
second_line = input().split()
third_line = input().split()

player_one_score = 0
player_two_score = 0
draw = 0

