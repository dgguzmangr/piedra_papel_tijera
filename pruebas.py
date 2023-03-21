import os


# Gives game instructions and stores user input in the player_without_format variable and then converts it to lowercase
# in the player variable.
def start(player_name):
    player_without_format = input(f"{player_name} por favor ingresa tu jugada \n Para piedra ingresa 'piedra' "
                                  f"\n Para tijera ingresa 'tijera' "
                                  f"\n Para papel ingresa 'papel' "
                                  f"\n Tu jugada: ")
    player = player_without_format.lower()
    return player


# Processes the values stored in player and based on a condition that is true or not, updates the system_score and
# player_score variables by adding a point accordingly, also shows differentiated messages for each play result.
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


# The os module is imported to work with the operating system. With the name property the operating system is verified,
# if it is nt it is windows and the screen is cleared with cls, if it is Unix, Mac or Linux it is cleared with clear.
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def main(valid_options, system, player_score, system_score, player_name):
    while True:
        clear_screen()
        player = start(player_name)
        if player in valid_options:
            result = play(player, system, player_score, system_score, player_name)
            print(result)
            # update scores
            if "Ganaste" in result:
                player_score += 1
            elif "Perdiste" in result:
                system_score += 1
        else:
            print(f"{player} no es una opción válida.")
            clear_screen()
        play_again_without_format = input("¿Quires jugar de vuelta? "
                                          "\n pulsa 's' para continuar o cualquier letra para finalizar: ")
        play_again = play_again_without_format.lower()
        if play_again != "s":
            return f"Gracias por jugar " \
                   f"\n Marcador final: " \
                   f"\n {player_name}: {player_score} - Máquina: {system_score}"