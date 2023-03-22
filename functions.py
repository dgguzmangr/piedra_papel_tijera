import os

"""
Gives game instructions and stores user input in the player_without_format variable and then converts it to lowercase
in the player variable.
"""


def start(player_name):
    player_without_format = input(f"{player_name} por favor ingresa tu jugada \n Para piedra ingresa 'piedra' "
                                  f"\n Para tijera ingresa 'tijera' "
                                  f"\n Para papel ingresa 'papel' "
                                  f"\n Tu jugada: ")
    player = player_without_format.lower()
    return player


"""
Processes the values stored in player and based on a condition that is true or not, updates the system_score and
player_score variables by adding a point accordingly, also shows differentiated messages for each play result.
"""


def play(player, system, player_score, system_score, player_name):
    # tie
    if player == system:
        return (f"Juego: "
                f"\n {player_name}: {player} - Máquina: {system}"
                f"\n Empate!"
                f"\n Marcador:"
                f"\n {player_name}: {player_score} - Máquina: {system_score}")
    # player wins
    elif player == "piedra" and system == "tijera":
        player_score += 1
        return (f"Juego: "
                f"\n {player_name}: {player} - Máquina: {system}"
                f"\n Ganaste!"
                f"\n Piedra le gana a tijera!"
                f"\n Marcador:"
                f"\n {player_name}: {player_score} - Máquina: {system_score}")
    elif player == "papel" and system == "piedra":
        player_score += 1
        return (f"Juego: "
                f"\n {player_name}: {player} - Máquina: {system}"
                f"\n Ganaste!"
                f"\n Papel le gana a piedra!"
                f"\n Marcador:"
                f"\n {player_name}: {player_score} - Máquina: {system_score}")
    elif player == "tijera" and system == "papel":
        player_score += 1
        return (f"Juego: "
                f"\n {player_name}: {player} - Máquina: {system}"
                f"\n Ganaste!"
                f"\n Tijera le gana a papel!"
                f"\n Marcador:"
                f"\n {player_name}: {player_score} - Máquina: {system_score}")
    # system wins
    elif system == "piedra" and player == "tijera":
        system_score += 1
        return (f"Juego: "
                f"\n {player_name}: {player} - Máquina: {system}"
                f"\n Perdiste!"
                f"\n Piedra le gana a tijera!"
                f"\n Marcador:"
                f"\n {player_name}: {player_score} - Máquina: {system_score}")

    elif system == "papel" and player == "piedra":
        system_score += 1
        return (f"Juego: "
                f"\n {player_name}: {player} - Máquina: {system}"
                f"\n Perdiste!"
                f"\n Papel le gana a piedra!"
                f"\n Marcador:"
                f"\n {player_name}: {player_score} - Máquina: {system_score}")
    elif system == "tijera" and player == "papel":
        system_score += 1
        return (f"Juego: "
                f"\n {player_name}: {player} - Máquina: {system}"
                f"\n Perdiste!"
                f"\n Tijera le gana a papel!"
                f"\n Marcador:"
                f"\n {player_name}: {player_score} - Máquina: {system_score}")


"""
The os module is imported to work with the operating system. With the name property the operating system is verified,
if it is nt it is windows and the screen is cleared with cls, if it is Unix, Mac or Linux it is cleared with clear.
"""


def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


"""
It calls the start function and saves it in the player variable. Verifies that the user's move (player) is valid, 
that is, that it is among the values stored in the valid_options list. If included in valid_options, the play 
function is stored in the result variable and result is printed. Then the player_score and system_score variables are 
updated.. In case player is not in valid_options a message is printed. The user is then asked if they want to continue
 playing and a loop is created. Then the clear_screen function is called to clear the screen. At the end the final 
 score is shown.
"""


def option1(valid_options, system, player_score, system_score, player_name):
    while True:
        clear_screen()
        player = start(player_name)
        if player in valid_options:
            result = play(player, system, player_score, system_score, player_name)
            print(result)
            if "Ganaste" in result:
                player_score += 1
            elif "Perdiste" in result:
                system_score += 1
        else:
            print(f"{player} no es una opción válida.")
            clear_screen()
        play_again_without_format = input("¿Quieres jugar de vuelta? "
                                          "\n pulsa 's' para continuar o cualquier letra para finalizar: ")
        play_again = play_again_without_format.lower()
        if play_again != "s":
            print(f"Gracias por jugar "
                  f"\n Marcador final: "
                  f"\n {player_name}: {player_score} - Máquina: {system_score}")
        return f"Gracias por jugar \n Marcador final: \n {player_name}: {player_score} - Máquina: {system_score}"


"""
Create a counter (count) and initialize it to 0. Then in a while loop with a max condition of 3 for count:
It calls the start function and saves it in the player variable. Verifies that the user's move (player) is valid,
that is, that it is among the values stored in the valid_options list. If included in valid_options, the play function
is stored in the result variable and result is printed. Then the player_score and system_score variables are updated.
In case player is not in valid_options a message is printed. The user is then asked if they want to continue playing,
 given the option to exit, and a loop is created. At the end the final score is shown.
"""


def option2(valid_options, system, player_score, system_score, player_name):
    count = 0
    while count < 3:

        player = start(player_name)
        if player in valid_options:
            result = play(player, system, player_score, system_score, player_name)
            print(result)
            if "Ganaste" in result:
                player_score += 1
            elif "Perdiste" in result:
                system_score += 1
        else:
            print(f"{player} no es una opción válida.")
            system_score += 1

        count += 1
    return f"Gracias por jugar " \
           f"\n Marcador final 3/3: " \
           f"\n {player_name}: {player_score} - Máquina: {system_score}"


"""
It creates a round counter and initializes it to 0. Then with a while loop the option2 function is repeated 3 times.
Then, with a conditional, choose whether the user or the machine wins the round by choosing which number is greater.
In each case of the conditional, the variables player_round_score and system_round_score are increased accordingly.
Finally returns the round frame.
"""


def option3(valid_options, system, player_score, system_score, player_name, player_round_score, system_round_score):
    round_count = 0
    while round_count < 3:
        option2(valid_options, system, player_score, system_score, player_name)
        if system_score > player_score:
            print(f"{player_name}, perdiste esta ronda")
            system_round_score += 1
        else:
            print(f"{player_name} ganaste esta ronda!!!")
            player_round_score += 1
        round_count += 1
    return f"Gracias por jugar " \
           f"\n Marcador de ronda final: " \
           f"\n {player_name}: {player_round_score} - Máquina: {system_round_score}"


def menu(valid_options, system, player_score, system_score, player_name, player_round_score, system_round_score):
    while True:
        print("----------------- PIEDRA, PAPEL O TIJERA ----------------- \n"
              "JUEGO SIMPLE (1) ---- RONDA DE 3 (2) ---- 3 RONDAS DE 3 (3) \n")
        game = input("------------ Pulse 1, 2 0 3 según su elección ------------ \n"
                     "Tu elección: ")
        if game == "1":
            option1(valid_options, system, player_score, system_score, player_name)
        elif game == "2":
            option2(valid_options, system, player_score, system_score, player_name)
        elif game == "3":
            option3(valid_options, system, player_score, system_score, player_name, player_round_score,
                    system_round_score)
        else:
            confirmation_without_format = input(f"f{player_name} no es una opción válida, "
                                                "¿Quieres intentarlo de nuevo (s) o quieres salir (e)?")
            confirmation = confirmation_without_format.lower()
            if confirmation == "s":
                continue
            else:
                return
        # close_game = input("Para salir de juego presiona (e)")
        # if close_game == "e":
            # break
