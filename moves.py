
#This module contains all of the functions which move pieces on the board
#each function attempts the move given input data (piece, row, col)
#import board to check status of a piece adn modify piece positions
import board_info as board
#function for getting column number and getting column letter
def get_col_num(col):
    if (col == 'a'): return 0
    elif (col == 'b'): return 1
    elif (col == 'c'): return 2
    elif (col == 'd'): return 3
    elif (col == 'e'): return 4
    elif (col == 'f'): return 5
    elif (col == 'g'): return 6
    elif (col == 'h'): return 7
    else: return 'there was a problem'
def get_col_letter(col):
    if (col == 0): return 'a'
    elif (col == 1): return 'b'
    elif (col == 2): return 'c'
    elif (col == 3): return 'd'
    elif (col == 4): return 'e'
    elif (col == 5): return 'f'
    elif (col == 6): return 'g'
    elif (col == 7): return 'h'
#functions for moving each piece, the appropriate position is checked on the board
#returns 'invalid move' if an invalid move is made
#returns 'cannot take your own piece' if a piece of the same color is on the desired space
#see pawn functions for special errors involving the pawn
def move_pawn(board_instance, color, current_row, current_col, proposed_row, proposed_col):
    available_spaces = [] #['a1', 'a2'] where the first number is the column and the second is the row
    check = []
    current_col_num = get_col_num(current_col)
    #returns three special errors: 'cannot attack forward' , 'no piece to attack diagonally' and 'cannot move backwards'
    #calculate available spaces
    #check one space ahead and spaces diagonal which have pieces
    #check = [[row, column],[row, column]] spacial case where the second two need to be occupied for the piece to be moved
    if (color == 'black'): check = [
        [current_row+1,current_col_num],
        [current_row+1,current_col_num-1],
        [current_row+1,current_col_num+1]
    ]
    else: check = [
        [current_row-1,current_col_num],
        [current_row-1,current_col_num-1],
        [current_row-1,current_col_num+1]
    ]
    if (color == 'white'):
        if board_instance.check_presence(check[0][0], check[0][1]): available_spaces.append(str(check[0][1])+str(check[0][0]))
        if not board_instance.check_presence(check[1][0], check[1][1]): available_spaces.append(str(check[1][1])+str(check[1][0]))
        if not board_instance.check_presence(check[2][0], check[2][1]): available_spaces.append(str(check[2][1])+str(check[2][0]))
    else:
        if not board_instance.check_presence(check[0][0], check[0][1]): 
            available_spaces.append(str(check[0][1])+str(check[0][0]))
            print('correct piece appended :D')
        if not board_instance.check_presence(check[1][0], check[1][1]): 
            available_spaces.append(str(check[1][1])+str(check[1][0]))
            print('not 1')
        #for some reason the result of check_presence changes once a black pawn passes row 5 (current_row > 5)
        if (current_row > 4):
            if not board_instance.check_presence(check[2][0], check[2][1]): 
                available_spaces.append(str(check[2][1])+str(check[2][0]))
                print('not 2 1')
            if board_instance.check_presence(check[0][0], check[0][1]): 
                available_spaces.append(str(check[0][1])+str(check[0][0]))
                print('correct piece appended :D')
        else:
            if board_instance.check_presence(check[2][0], check[2][1]): 
                available_spaces.append(str(check[2][1])+str(check[2][0]))
                print('not 2 2')
    print('available spaces: ',available_spaces)
    #check if proposed move is an available space
    proposed_col_num = get_col_num(proposed_col)
    print('proposed move:',str(proposed_col_num)+str(proposed_row))
    availability = str(proposed_col_num)+str(proposed_row) in available_spaces
    print('availablility is',availability)
    #move the piece
    #print move information
    if availability: 
        test = board_instance.set_status(get_col_num(proposed_col),proposed_row,'pawn_'+color)
        board_instance.set_status(get_col_num(current_col),current_row, 'empty')
        print('move status: ',test)
        print('pawn moved from '+str(current_row)+current_col+' to '+str(proposed_row)+proposed_col)
        return True
    else: return False
def move_rook(board_instance, color, current_row, current_col, proposed_row, proposed_col):
    #more debug logs
    print('move_rook function works!')
    print('board_instance: '+str(board_instance))
    print('current_row:    '+str(current_row))
    print('current_col:    '+str(current_col))
    print('proposed_row:   '+str(proposed_row))
    print('proposed_col:   '+str(proposed_col))
    ################
    available_spaces = []
    current_col_num = get_col_num(current_col)
    #calculate available spaces
    #check spanes in 4 directions until a space is occupied
    #up i
    i=0
    while True:
        if not board_instance.check_presence(current_row+i, current_col_num): 
            available_spaces.append(str(current_col)+str(current_row+i))
            i+=1
        elif board_instance.check_presence(current_row+i, current_col_num): 
            available_spaces.append(str(current_col)+str(current_row+i))
            break
    #left i
    i=0
    while True:
        if not board_instance.check_presence(current_row, current_col_num-i):
            available_spaces.append(str(get_col_letter(current_col_num-i))+str(current_row))
            i+=1
        elif board_instance.check_presence(current_row, current_col_num-i):
            available_spaces.append(str(get_col_letter(current_col_num-i))+str(current_row))
            break
    #right i
    i=0
    while True:
        if not board_instance.check_presence(current_row, current_col_num+i):
            available_spaces.append(str(get_col_letter(current_col_num+i))+str(current_row))
            i+=1
        elif board_instance.check_presence(current_row, current_col_num+i):
            available_spaces.append(str(get_col_letter(current_col_num+i))+str(current_row))
            break
    #down i
    i=0
    while True:
        if not board_instance.check_presence(current_row-i, current_col_num): 
            available_spaces.append(str(current_col)+str(current_row-i))
            i+=1
        elif board_instance.check_presence(current_row+i, current_col_num): 
            available_spaces.append(str(current_col)+str(current_row-i))
            break
    #check if proposed move is an available space
    print('available space: ',available_spaces)
    availability = str(proposed_row)+str(proposed_col) in available_spaces
    #move the piece
    #print move information
    if availability: 
        print('rook moved from '+str(current_row)+current_col+' to '+str(proposed_row)+proposed_col)
        board_instance.set_status(get_col_num(proposed_col),proposed_row,'rook_'+color)#TODO add color params FUCK
        board_instance.set_status(get_col_num(current_col),current_row, 'empty')
        return True
    else: return False
def move_knight(board_instance, color, current_row, current_col, proposed_row, proposed_col):
    #calculate available spaces
    #check = [[row, column],[row, column]] the available spaces for now are hard coded
    current_col_num = get_col_num(current_col)
    #TODO try catch for index errors and 
    check = [
        [current_row+1, current_col_num-3],
        [current_row+3, current_col_num-1],
        [current_row+3, current_col_num+1],
        [current_row+1, current_col_num+3],
        [current_row-1, current_col_num-3],
        [current_row-3, current_col_num-1],
        [current_row-3, current_col_num+1],
        [current_row-1, current_col_num+3]
    ]
    print('col letter test: ',get_col_letter(check[0][1]),'col test: ',check[0][1])
    available_spaces = [
        str(get_col_letter(check[0][1]))+str(check[0][0]),
        str(get_col_letter(check[1][1]))+str(check[1][0]),
        str(get_col_letter(check[2][1]))+str(check[2][0]),
        str(get_col_letter(check[3][1]))+str(check[3][0]),
        str(get_col_letter(check[4][1]))+str(check[4][0]),
        str(get_col_letter(check[5][1]))+str(check[5][0]),
        str(get_col_letter(check[6][1]))+str(check[6][0]),
        str(get_col_letter(check[7][1]))+str(check[7][0])
    ]
    #check is proposed move is an available space
    availability = str(proposed_row)+str(proposed_col) in available_spaces
    #move the piece
    #pirnt the result
    if availability: 
        print('knight moved from '+str(current_row)+current_col+' to '+str(proposed_row)+proposed_col)
        board_instance.set_status(get_col_num(proposed_col),proposed_row,'knight_'+color)#TODO add color params
        board_instance.set_status(get_col_num(current_col),current_row, 'empty')
        return True
    else: return False
def move_bishop(board_instance, current_row, current_col, proposed_row, proposed_col):
    available_spaces = []
    current_col_num = get_col_num(current_col)
    #calculate available spaces
    #check spanes in 4 directions until a space is occupied
    #up right i+i
    i=0
    while True:
        if not board_instance.check_presence(current_row+i, current_col_num+i): 
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row+i)
            i+=1
        elif board_instance.check_presence(current_row+i, current_col_num+i): 
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row+i)
            break
    #up left i-i
    i=0
    while True:
        if not board_instance.check_presence(current_row+i, current_col_num-i):
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row+i)
            i+=1
        elif board_instance.check_presence(current_row, current_col_num-i):
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row)
            break
    #down right -i+i
    i=0
    while True:
        if not board_instance.check_presence(current_row-i, current_col_num+i):
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row-i)
            i+=1
        elif board_instance.check_presence(current_row-i, current_col_num+i):
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row-i)
            break
    #down left -i-i
    i=0
    while True:
        if not board_instance.check_presence(current_row-i, current_col_num-i): 
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row-i)
            i+=1
        elif board_instance.check_presence(current_row-i, current_col_num-i): 
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row-i)
            break
    #check if proposed move is an available space
    availability = str(proposed_row)+str(proposed_col) in available_spaces
    #move the piece
    #print move information
    if availability: 
        print('bishop moved from '+str(current_row)+current_col+' to '+str(proposed_row)+proposed_col)
        board_instance.set_status(get_col_num(proposed_col),proposed_row,'bishop_'+color)#TODO add color params [censored]
        board_instance.set_status(get_col_num(current_col),current_row, 'empty')
        return True
    else: return False
def move_queen(board_instance, current_row, current_col, proposed_row, proposed_col):
    available_spaces = []
    current_col_num = get_col_num(current_col)
    #calculate available spaces
    #borrowed from rook code
    #up i
    i=0
    while True:
        if not board_instance.check_presence(current_row+i, current_col_num): 
            available_spaces.append(str(current_col)+current_row+i)
            i+=1
        elif board_instance.check_presence(current_row+i, current_col_num): 
            available_spaces.append(str(current_col)+current_row+i)
            break
    #left i
    i=0
    while True:
        if not board_instance.check_presence(current_row, current_col_num-i):
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row)
            i+=1
        elif board_instance.check_presence(current_row, current_col_num-i):
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row)
            break
    #right i
    i=0
    while True:
        if not board_instance.check_presence(current_row, current_col_num+i):
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row)
            i+=1
        elif board_instance.check_presence(current_row, current_col_num+i):
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row)
            break
    #down i
    i=0
    while True:
        if not board_instance.check_presence(current_row-i, current_col_num): 
            available_spaces.append(str(current_col)+current_row-i)
            i+=1
        elif board_instance.check_presence(current_row+i, current_col_num): 
            available_spaces.append(str(current_col)+current_row-i)
            break
    #borrowed from bishop code
    #up right i+i
    i=0
    while True:
        if not board_instance.check_presence(current_row+i, current_col_num+i): 
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row+i)
            i+=1
        elif board_instance.check_presence(current_row+i, current_col_num+i): 
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row+i)
            break
    #up left i-i
    i=0
    while True:
        if not board_instance.check_presence(current_row+i, current_col_num-i):
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row+i)
            i+=1
        elif board_instance.check_presence(current_row, current_col_num-i):
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row)
            break
    #down right -i+i
    i=0
    while True:
        if not board_instance.check_presence(current_row-i, current_col_num+i):
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row-i)
            i+=1
        elif board_instance.check_presence(current_row-i, current_col_num+i):
            available_spaces.append(str(get_col_letter(current_col_num+i))+current_row-i)
            break
    #down left -i-i
    i=0
    while True:
        if not board_instance.check_presence(current_row-i, current_col_num-i): 
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row-i)
            i+=1
        elif board_instance.check_presence(current_row-i, current_col_num-i): 
            available_spaces.append(str(get_col_letter(current_col_num-i))+current_row-i)
            break
    #check if proposed move is an available space
    availablility = str(proposed_row)+str(proposed_col) in available_spaces
    #move the piece
    #print move information
    if availability: 
        print('queen moved from '+str(current_row)+current_col+' to '+str(proposed_row)+proposed_col)
        board_instance.set_status(get_col_num(proposed_col),proposed_row,'queen_'+color)#TODO add color params FUCK
        board_instance.set_status(get_col_num(current_col),current_row, 'empty')
        return True
    else: return False
def move_king(board_instance, current_row, current_col, proposed_row, proposed_col): #TODO: deny the move if the king is going to be in check
    current_col_num = get_col_num(current_col)
    #calculate available spaces
    check = [
        [current_row+1, current_col_num],
        [current_row+1, current_col_num+1],
        [current_row, current_col_num+1],
        [current_row-1, current_col_num+1],
        [current_row-1, current_col_num],
        [current_row-1, current_col_num-1],
        [current_row, current_col_num-1],
        [current_row+1, current_col_num-1]
    ]
    available_spaces = [
        get_col_letter(check[0][1])+str(check[0][0]),
        get_col_letter(check[0][1])+str(check[1][0]),
        get_col_letter(check[0][1])+str(check[2][0]),
        get_col_letter(check[0][1])+str(check[3][0]),
        get_col_letter(check[0][1])+str(check[4][0]),
        get_col_letter(check[0][1])+str(check[5][0]),
        get_col_letter(check[0][1])+str(check[6][0]),
        get_col_letter(check[0][1])+str(check[7][0])
    ]
    #check is proposed move is an available space
    availability = str(proposed_row)+str(proposed_col) in available_spaces
    #move the piece
    #pirnt the result
    if availability: 
        print('king moved from '+str(current_row)+current_col+' to '+str(proposed_row)+proposed_col)
        board_instance.set_status(get_col_num(proposed_col),proposed_row,'king_'+color)#TODO add color params [censored]
        board_instance.set_status(get_col_num(current_col),current_row, 'empty')
        return True
    else: return False
#get the piece and then send data to the appropriate function then returns relevant information about the move
def move(board_instance, piece, current_row, current_col, proposed_row, proposed_col):
    piece_info = piece.split('_')
    print('piece is',piece)
    print('piece info: ',piece_info)
    piece_type = piece_info[0]
    piece_color = piece_info[1]
    if (piece_type == 'pawn'): return move_pawn(board_instance, piece_color, current_row, current_col, proposed_row, proposed_col)
    elif (piece_type == 'rook'): return move_rook(board_instance, piece_color, current_row, current_col, proposed_row, proposed_col)
    elif (piece_type == 'knight'): return move_knight(board_instance, current_row, current_col, proposed_row, proposed_col)
    elif (piece_type == 'bishop'): return move_bishop(board_instance, current_row, current_col, proposed_row, proposed_col)
    elif (piece_type == 'king'): return move_king(board_instance, current_row, current_col, proposed_row, proposed_col)
    elif (piece_type == 'queen'): return move_queen(board_instance, current_row, current_col, proposed_row, proposed_col)
    else: return 'this is not a piece'