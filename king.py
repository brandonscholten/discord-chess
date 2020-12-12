
#script for chekcing the status of the king at any given point in the game
#functions return False, 'check', or 'checkmate'
#global vars because nested function namespace in python is [censored] and almost made me cry
up = ''
left = ''
right = ''
down = ''
up_left = ''
up_right = ''
down_left = ''
down_right = ''
up_i_state = 0
left_i_state = 0
right_i_state = 0
down_i_state = 0
up_left_i_state = 0
up_right_i_state = 0
down_left_i_state = 0
down_right_i_state = 0

def check(instance, color):
    check = False
    mate = False
    #find the piece in the matrice
    king_col = 0
    king_row = 0
    piece = ''
    for x in range(8):
        for y in range(8):
            proposed_piece = instance.get_status(x,y)
            #print('getting status for (',x,',',y,')...')
            #print('x is ',x)
            #print('y is ',y)
            #print('looking for king_'+color+' found '+proposed_piece[:])
            if (proposed_piece[4:] == 'king_'+color):
                #print('found king...')
                piece = proposed_piece
                king_col = x
                king_row = y
    #get available spaces
    available_spaces = [
        [king_row+1, king_col],
        [king_row+1, king_col+1],
        [king_row, king_col+1],
        [king_row-1, king_col+1],
        [king_row-1, king_col],
        [king_row-1, king_col-1],
        [king_row, king_col-1],
        [king_row+1, king_col-1]
    ]
    #check pieces in each direction of the king
    def check_space():
        #add variables
        global up, left, right, down, up_left, up_right, down_left, down_right, up_i_state, left_i_state, right_i_state, down_i_state, up_left_i_state, up_right_i_state, down_left_i_state, down_right_i_state
        #up i
        #print('checking up...')
        i=1
        while True:
            if not instance.check_presence(king_row+i, king_col): i+=1
            elif instance.check_presence(king_row+i, king_col): 
                up = instance.get_status(king_col, king_row+i)
                up_i_state = i
                print('up is',up,'and i is',i)
                break
        #left i
        #print('checking left...')
        i=1
        while True:
            if not instance.check_presence(king_row, king_col-i): i+=1
            elif instance.check_presence(king_row, king_col-i):
                left = instance.get_status(king_col-i, king_row)
                left_i_state = i
                break
        #right i
        #print('checking right...')
        i=1
        while True:
            if not instance.check_presence(king_row, king_col+i): i+=1
            elif instance.check_presence(king_row, king_col+i):
                right = instance.get_status(king_col+i, king_row)
                right_i_state = i
                break
        #down i
        #print('checking down...')
        i=1
        while True:
            if not instance.check_presence(king_row-i, king_col): i+=1
            elif instance.check_presence(king_row-i, king_col): 
                down = instance.get_status(king_col, king_row-i)
                down_i_state = i
                break
        #borrowed from bishop code
        #up right i+i
        #print('checking up right..')
        i=1 
        while True:
            if not instance.check_presence(king_row+i, king_col+i): i+=1
            elif instance.check_presence(king_row+i, king_col+i): 
                up_right = instance.get_status(king_col+i, king_row+i)
                up_right_i_state = i
                break
        #up left i-i
        #print('checking up left...')
        i=1
        while True:
            if not instance.check_presence(king_row+i, king_col-i): i+=1
            elif instance.check_presence(king_row+i, king_col-i):
                up_left = instance.get_status(king_col-i, king_row+i)
                up_left_i_state = i
                break
        #down right -i+i
        #print('checking down right...')
        i=1
        while True:
            if not instance.check_presence(king_row-i, king_col+i): i+=1
            elif instance.check_presence(king_row-i, king_col+i):
                down_right = instance.get_status(king_col+i, king_row-i)
                down_right_i_state = i
                break
        #down left -i-i
        #print('checking down left...')
        i=1
        while True:
            if not instance.check_presence(king_row-i, king_col-i): i+=1
            elif instance.check_presence(king_row-i, king_col-i): 
                down_left = instance.get_status(king_col-i, king_row-i)
                down_left_i_state = i
                break
    check_space()
    #print('summary:')
    #print('u:',up)
    #print('r:',right)
    #print('l:',left)
    #print('d:',down)
    #print('ur:',up_right)
    #print('ul:',up_left)
    #print('dr:',down_right)
    #print('dl:',down_left)
    def check_check():
        #check whether or not that piece can take the king
        #up
        try:
            print('checking up.. up is',up)
            upArr = up.split('_')
            if (upArr[2] == 'pawn'): check = False
            elif (upArr[2] == 'rook'): check = True
            elif (upArr[2] == 'bishop'): check = False
            elif (upArr[2] == 'knight'): check = False
            elif (upArr[2] == 'king'): 
                if (up_i_state > 1): check = False
                else: check = True
            elif (upArr[2] == 'queen'): check = True
            else: print('I am suffering on line 121') 
        except IndexError: print('space does not exist')
        #left
        try:
            leftArr = left.split('_')
            if (leftArr[2] == 'pawn'): check = False
            elif (leftArr[2] == 'rook'): check = True
            elif (leftArr[2] == 'bishop'): check = False
            elif (leftArr[2] == 'knight'): check = False
            elif (leftArr[2] == 'king'): 
                if (left_i_state > 1): check = False
                else: check = True
            elif (leftArr[2] == 'queen'): check = True
            else: print('I am suffering on line 132') 
        except IndexError: print('space does not exist')
        #right
        try:
            rightArr = right.split('_')
            if (rightArr[2] == 'pawn'): check = False
            elif (rightArr[2] == 'rook'): check = True
            elif (rightArr[2] == 'bishop'): check = False
            elif (rightArr[2] == 'knight'): check = False
            elif (rightArr[2] == 'king'): 
                if (right_i_state > 1): check = False
                else: check = True
            elif (rightArr[2] == 'queen'): check = True
            else: print('I am suffering on line 143') 
        except IndexError: print('space does not exist')
        #down
        try:
            downArr = down.split('_')
            if (downArr[2] == 'pawn'): check = False
            elif (downArr[2] == 'rook'): check = True
            elif (downArr[2] == 'bishop'): check = False
            elif (downArr[2] == 'knight'): check = False
            elif (downArr[2] == 'king'): 
                if (down_i_state > 1): check = False
                else: check = True
            elif (upArr[2] == 'queen'): check = True
            else: print('I am suffering on line 154') 
        except IndexError: print('space does not exist')
        #up_right
        try:
            up_rightArr = up_right.split('_')
            if (up_rightArr[2] == 'pawn'): 
                if (up_right_i_state > 1): check = False
                else: check = True
            elif (up_rightArr[2] == 'rook'): check = False
            elif (up_rightArr[2] == 'bishop'): check = True
            elif (up_rightArr[2] == 'knight'): check = False
            elif (up_rightArr[2] == 'king'): 
                if (up_right_i_state > 1): check = False
                else: check = True
            elif (up_rightArr[2] == 'queen'): check = True
            else: print('I am suffering on line 165') 
        except IndexError: print('space does not exist')
        #up_left
        try:
            up_leftArr = up_left.split('_')
            if (up_leftArr[2] == 'pawn'): 
                if (up_left_i_state > 1): check = False
                else: check = True
            elif (up_leftArr[2] == 'rook'): check = False
            elif (up_leftArr[2] == 'bishop'): check = True
            elif (up_leftArr[2] == 'knight'): check = False
            elif (up_leftArr[2] == 'king'): 
                if (up_left_i_state > 1): check = False
                else: check = True
            elif (up_leftArr[2] == 'queen'): check = True
            else: print('I am suffering on line 176') 
        except IndexError: print('space does not exist')
        #down_right
        try:
            down_rightArr = down_right.split('_')
            if (down_rightArr[2] == 'pawn'):
                if (down_right_i_state > 1): check = False
                else: check = True
            elif (down_rightArr[2] == 'rook'): check = False
            elif (down_rightArr[2] == 'bishop'): check = True
            elif (down_rightArr[2] == 'knight'): check = False
            elif (down_rightArr[2] == 'king'): 
                if (down_right_i_state > 1): check = False
                else: check = True
            elif (down_rightArr[2] == 'queen'): check = True
            else: print('I am suffering on line 187') 
        except IndexError: print('space does not exist')
        #down_left
        try:
            down_leftArr = down_left.split('_')
            if (down_leftArr[2] == 'pawn'): 
                if (down_left_i_state > 1): check = False
                else: check = True
            elif (down_leftArr[2] == 'rook'): check = False
            elif (down_leftArr[2] == 'bishop'): check = True
            elif (down_leftArr[2] == 'knight'): check = False
            elif (down_leftArr[2] == 'king'): 
                if (down_left_i_state > 1): check = False
                else: check = True
            elif (down_leftArr[2] == 'queen'): check = True
            else: print('I am suffering on line 198') 
        except IndexError: print('space does not exist')
        #knight
        try:
            if (instance.get_status(king_col-3, king_row+1)): check = True
            elif (instance.get_status(king_col-1, king_row+3)): check = True
            elif (instance.get_status(king_col+1, king_row+3)): check = True
            elif (instance.get_status(king_col+3, king_row+1)): check = True
            elif (instance.get_status(king_col-3, king_row-1)): check = True
            elif (instance.get_status(king_col-1, king_row-3)): check = True
            elif (instance.get_status(king_col+1, king_row-3)): check = True
            elif (instance.get_status(king_col+3, king_row-1)): check = True
            else: check = False
        except IndexError: print('space does not exist')
    check_check()
    #if check is true, check each space around the king
    if check:
        #set original vars
        original_col = king_col
        original_row = king_row
        #set vars
        king_col = available_spaces[0][1]
        king_row = available_spaces[0][0]
        #run function
        check_space()
        #if check is true remove the space from available spaces
        if check: del available_spaces[0]
        #if the spaces are filled or in danger then remove them from available spaces
        #set vars
        king_col = available_spaces[1][1]
        king_row = available_spaces[1][0]
        #run function
        check_space()
        #if check is true remove the space from available spaces
        if check: del available_spaces[0]
        #if the spaces are filled or in danger then remove them from available spaces
        #set vars
        king_col = available_spaces[2][1]
        king_row = available_spaces[2][0]
        #run function
        check_space()
        #if check is true remove the space from available spaces
        if check: del available_spaces[0]
        #if the spaces are filled or in danger then remove them from available spaces
        #set vars
        king_col = available_spaces[3][1]
        king_row = available_spaces[3][0]
        #run function
        check_space()
        #if check is true remove the space from available spaces
        if check: del available_spaces[0]
        #if the spaces are filled or in danger then remove them from available spaces
        #set vars
        king_col = available_spaces[4][1]
        king_row = available_spaces[4][0]
        #run function
        check_space()
        #if check is true remove the space from available spaces
        if check: del available_spaces[0]
        #if the spaces are filled or in danger then remove them from available spaces
        #set vars
        king_col = available_spaces[5][1]
        king_row = available_spaces[5][0]
        #run function
        check_space()
        #if check is true remove the space from available spaces
        if check: del available_spaces[0]
        #if the spaces are filled or in danger then remove them from available spaces
        #set vars
        king_col = available_spaces[6][1]
        king_row = available_spaces[6][0]
        #run function
        check_space()
        #if check is true remove the space from available spaces
        if check: del available_spaces[0]
        #if the spaces are filled or in danger then remove them from available spaces
        #set vars
        king_col = available_spaces[7][1]
        king_row = available_spaces[7][0]
        #run function
        check_space()
        #reset
        check = True
        king_col = original_col
        king_row = original_row
    #if check is true remove the space from available spaces
    if check: del available_spaces[0]
    #if the spaces are filled or in danger then remove them from available spaces
    #if available_spaces is empty, mate is True
    if (len(available_spaces) == 0): mate = True
    #return result
    if mate: return 'checkmate'
    if check: return 'mate'
    else: return False