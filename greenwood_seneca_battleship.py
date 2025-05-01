'''
    Prints the boards with symbols that are required for play

    Args: All boards for computer and user

    Returns: A board with emojis to represent the different events that are happening in the game
    '''
import sys
import random

def display_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print("")


def coordinate_converter(user_guess):
    mapping = {
        "A1": (1, 1), "A2": (3, 1), "A3": (5, 1), "A4": (7, 1), "A5": (9, 1),
        "B1": (1, 3), "B2": (3, 3), "B3": (5, 3), "B4": (7, 3), "B5": (9, 3),
        "C1": (1, 5), "C2": (3, 5), "C3": (5, 5), "C4": (7, 5), "C5": (9, 5),
        "D1": (1, 7), "D2": (3, 7), "D3": (5, 7), "D4": (7, 7), "D5": (9, 7),
        "E1": (1, 9), "E2": (3, 9), "E3": (5, 9), "E4": (7, 9), "E5": (9, 9)
    }
    return mapping.get(user_guess, (None, None))


def place_ships(board):
    counter = 0
    while counter < 4:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if row % 2 == 1 and col % 2 == 1:
            if board[row][col] == "👋":
                board[row][col] = "🚢"
                counter += 1


def main():
    #boards to attack and defend in both user and computer
    user_attack_board = [
        ["----A----B----C----D----E--"],
        ['1|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['2|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['3|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['4|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['5|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['           ATTACK         ']
    ]


    user_defense_board = [
        ["----A----B----C----D----E--"],
        ['1|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['2|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['3|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['4|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['5|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['          WARSHIPS        ']
    ]


    comp_defense_board = [
        ["----A----B----C----D----E--"],
        ['1|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['2|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['3|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['4|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['5|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['          C_WARSHIPS        ']
    ]


    comp_attack_board = [
        ["----A----B----C----D----E--"],
        ['1|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['2|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['3|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['4|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['5|', "👋", '|', "👋", '|', "👋", '|', "👋", '|', "👋", '|'],
        ["---------------------------"],
        ['           C_ATTACK         ']
    ]


    place_ships(comp_defense_board)
    place_ships(user_defense_board)


    print("Welcome to Battleship! Here are the boards")
    print("User Board:")
    display_board(user_attack_board)
    print("Computer Board:")
    display_board(comp_attack_board)


    turns = random.choice([True, False])
    user_hit_counter = 0
    comp_hit_counter = 0
    #begins the game with hit counter being zero 

    valid_inputs = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", "E1", "E2", "E3", "E4", "E5"]


    comp_available_guesses = valid_inputs.copy()


    while True:
        if turns: # if user turn
            print("Your turn:")
            user_turn_active = True
            while user_turn_active:
                user_guess = input("Pick a coordinate (e.g., A1, B3): ").upper() # ask for user input
                if user_guess in valid_inputs: # only process valid coordinates
                    row, col = coordinate_converter(user_guess) # converts the guess
                    if comp_defense_board[row][col] == "👋":
                        user_attack_board[row][col] = "🚫" # mark miss
                        comp_defense_board[row][col] = "🚫"
                        display_board(user_attack_board)
                        user_turn_active = False  # end user turn
                        turns = False # switch to computer
                    elif comp_defense_board[row][col] == "🚢":
                        user_attack_board[row][col] = "💥" # mark hit
                        comp_defense_board[row][col] = "💥"
                        user_hit_counter += 1 #adds to counter 
                        display_board(user_attack_board)
                        print("Hit! Go again.") # let user go again
                        if user_hit_counter == 4: # win condition
                            print("You win!")
                            sys.exit()
                    else:
                        print("Already guessed. Try again.")
                else:
                    print("Invalid input. Try again.")


        else: # if computer turn
            print("Computer's turn:")
            comp_turn_active = True
            while comp_turn_active:
                comp_guess = random.choice(comp_available_guesses) # take random valid guess
                comp_available_guesses.remove(comp_guess) # prevent future repeats
                row, col = coordinate_converter(comp_guess)
                print(f"Computer guesses {comp_guess}")
                if user_defense_board[row][col] == "👋":
                    comp_attack_board[row][col] = "🚫"
                    user_defense_board[row][col] = "🚫"
                    display_board(comp_attack_board)
                    comp_turn_active = False  # send computer turn
                    turns = True # switch to user
                elif user_defense_board[row][col] == "🚢":
                    comp_attack_board[row][col] = "💥"
                    user_defense_board[row][col] = "💥"
                    comp_hit_counter += 1
                    display_board(comp_attack_board)
                    print("Computer hit your ship! It goes again.")
                    if comp_hit_counter == 4:
                        print("Computer wins!")
                        sys.exit()


main()
