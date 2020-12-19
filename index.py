
#Brandon Scholten (final revision made at 9:22pm Wednesday December 3)
#CLI CHess is an attempt at a fully functional command based chess game which will hopefully evolve into a discord bot
#This is the main file for the chess game
#importing external classes and functions
import board_info #importing the chessboard class
import king
import moves
import os
#functions
def game():
    #main game function
    #settings up the board #piece naming convention: [column]_[row]_[piece]_[color]
    board = board_info.board(
        ['a_1_rook_black','b_1_knight_black','c_1_bishop_black','d_1_queen_black','e_1_king_black','f_1_bishop_black','g_1_knight_black','h_1_rook_black'],
        ['a_2_pawn_black','b_2_pawn_black','c_2_pawn_black','d_2_pawn_black','e_2_pawn_black','f_2_pawn_black','g_2_pawn_black','h_2_pawn_black'],
        ['a_3_empty','b_3_empty','c_3_empty','d_3_empty','e_3_empty','f_3_empty','g_3_empty','h_3_empty'],
        ['a_4_empty','b_4_empty','c_4_empty','d_4_empty','e_4_empty','f_4_empty','g_4_empty','h_4_empty'],
        ['a_5_empty','b_5_empty','c_5_empty','d_5_empty','e_5_empty','f_5_empty','g_5_empty','h_5_empty'],
        ['a_6_empty','b_6_empty','c_6_empty','d_6_empty','e_6_empty','f_6_empty','g_6_empty','h_6_empty'],
        ['a_7_pawn_white','b_7_pawn_white','c_7_pawn_white','d_7_pawn_white','e_7_pawn_white','f_7_pawn_white','g_7_pawn_white','h_7_pawn_white'],
        ['a_8_rook_white','b_8_knight_white','c_8_bishop_white','d_8_king_white','e_8_queen_white','f_8_bishop_white','g_8_knight_white','h_8_rook_white']
    )
    #function for saving the game
    def save_game():
        print('this features is coming soon!')
        #ask the user to name their save file
        #filename = input('What would you like to call this game? >')
        #save the game
        #board.save(filename)
    #get names for player one and player two
    player_1_name = 'player_1'
    player_2_name = 'player_2'
    try:
        player_1_name = input("Enter name for player 1 >")
        player_2_name = input("Enter name for player 2 >")
    except:
        print('invalid input, default names will be used.')
    #array containing stolen pieces for each player
    #player_1_pieces = [] TODO: add this feature in version 2 or something lol
    #player_2 peices = []
    #game loop (main loop and loop for each player turn until someone wins, saves the game, or quits)
    def player_1(check_mate):
        if (check_mate == 'checkmate'): return True
        elif (check_mate == 'check'): print('PLEASE MOVE OUT OF CHECK\nTHIS PROGRAM IS INCAPABLE OF DETECTING WHETHER YOUR NEXT MOVE IS VALID\nAND YOU COULD RUIN YOUR GAME')
        while True:
            print(player_1_name+"'s turn!")
            print('select piece:')
            try:
                current_row = int(input('row (1-8) >'))
                current_col = input('col (a-h) >')
            except:
                print('invalid input, please try again...')
                continue
            piece = board.get_status(current_col, current_row-1)
            piece_info = piece.split('_')
            piece = piece_info[-2]+'_'+piece_info[-1]
            check = board.check_presence(current_row, current_col)
            print('check is ',check)
            if check: 
                print('select move:')
                try:
                    proposed_row = int(input('row (1-8) >'))
                    proposed_col = input('col (a-h) >')
                except:
                    print('invalid input, please try again...')
                    continue
                moved = moves.move(board, piece, current_row, current_col, proposed_row, proposed_col)
                print('moved is', moved)
                if not moved: 
                    print('This piece could not be moved')
                    continue
                else: break
            else:
                print('Invalid selection!')
        board.display()
    def player_2(check_mate):
        if (check_mate == 'checkmate'): return True
        elif (check_mate == 'check'): print('PLEASE MOVE OUT OF CHECK\nTHIS PROGRAM IS INCAPABLE OF DETECTING WHETHER YOUR NEXT MOVE IS VALID\nAND YOU COULD RUIN YOUR GAME')
        while True:
            print(player_2_name+"'s turn!")
            print('select piece:')
            try:
                current_row = int(input('row (1-8) >'))
                current_col = input('col (a-h) >')
            except:
                print('invalid input, please try again...')
                continue
            piece = board.get_status(current_col, current_row-1)
            piece_info = piece.split('_')
            piece = piece_info[-2]+'_'+piece_info[-1]
            check = board.check_presence(current_row, current_col)
            if check: 
                print('select move:')
                try:
                    proposed_row = int(input('row (1-8) >'))
                    proposed_col = input('col (a-h) >')
                except:
                    print('invalid input, please try again...')
                    continue
                moved = moves.move(board, piece, current_row, current_col, proposed_row, proposed_col)
                if not moved: 
                    print('This piece could not be moved')
                    continue
                else: break
            else:
                print('Invalid selection!')
    #game loop
    winner_1 = ''
    winner_2 = ''
    while True:
        #os.system('clear')
        board.display()
        print('press s to save for later, q to quit, or any other key to continue', end=' ')
        selection = input()
        if (selection == 'q'):
            prompt = input('are you sure you want to quit? any unsaved progress will be lost! [y/n]')
            if (prompt == 'y'): break
            else: continue
        elif (selection == 's'): save_game()
        else:
            winner_2 = player_1(king.check(board, 'white'))
            winner_1 = player_2(king.check(board, 'black'))
        #return winner
        if winner_2: return player_2
        if winner_1: return player_1    

def resume_game():
    #function for loading game from save file
    print("nothing here yet")
#welcome message loop
while True:
    print("""
=================================================
| Welcome to my chess game!!!                   |
|                                               |
| I plan on building this into a chat bot,      |
| but for now it is a command-line application  |
| as a proof of concept.                        |
|                                               |
| If you want to follow the progress of this    |
| game, please check it out on my github:       |
| https://www.github.com/brandonscholten        |
|                                               |
| Report bugs to: clichessbugs@protonmail.com   |
|                                               |
| options:                                      |
| 1. new game                                   |
| 2. open saved game (coming soon)              |
| 3. quit program                               |
================================================+
    """)
    try:
        choice = input('> ')
    except:
        print('invalid input, please try again...')
        continue
    if (choice == '1'):
        try:
            winner = game()
        except:
            print('fatal error occured')
        try:
            print('Check mate! The winner is: '+winner)
        except: 
            print('goodbye')
    elif (choice == '2'):
        resume_game()
    elif (choice == '3'):
        break
    else: 
        print("Wrong choice!")
        break