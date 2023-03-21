import random
import functions

"""
Game rules:
Rock beats scissors
Scissors beats paper
Paper beats rock

This application can receive commands in upper or lower case, distinguishes incorrect commands, has a marker that
it shows the player the accumulated score, clears the screen with each new move and also shows differentiated 
messages for the result of each move. It has a three option menu. The first for a simple game that the user can
retry as many times as he wants. The second option gives a round of three tries and at the end the final score is 
printed. The third option gives three rounds of three and at the end gives the score for rounds.
"""
# variables
valid_options = ["piedra", "papel", "tijera"]
system = random.choice(valid_options)
player_score = 0
system_score = 0
player_round_score = 0
system_round_score = 0

player_name = input("Por favor ingresa tu nombre: ")
execute = functions.menu(valid_options,
                         system,
                         player_score,
                         system_score,
                         player_name,
                         player_round_score,
                         system_round_score)
print(execute)
