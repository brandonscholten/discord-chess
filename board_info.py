
#import assets
import assets
#import moves for get_col_letter function
import moves
#board class for managing chess board
#piece naming convention: [column]_[row]_[piece]_[color]
#chess board
class board:
    def __init__(self, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, board=[]):
        self.row_1 = row_1
        self.row_2 = row_2
        self.row_3 = row_3
        self.row_4 = row_4
        self.row_5 = row_5
        self.row_6 = row_6
        self.row_7 = row_7
        self.row_8 = row_8
        self.board = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8]

    #getters
    def get_status(self, column, row):
        #define column_number
        column_number = 0
        if (column == 'a'): column_number = 0
        elif (column  == 'b'): column_number = 1
        elif (column  == 'c'): column_number = 2
        elif (column  == 'd'): column_number = 3
        elif (column  == 'e'): column_number = 4
        elif (column  == 'f'): column_number = 5
        elif (column  == 'g'): column_number = 6
        elif (column  == 'h'): column_number = 7
        else: column_number = column
        #print('getting status... column number is: ',column_number, 'row is',row)
        #return status
        if (row == 0): return self.row_1[column_number]
        elif (row == 1): return self.row_2[column_number]
        elif (row == 2): return self.row_3[column_number]
        elif (row == 3): return self.row_4[column_number]
        elif (row == 4): return self.row_5[column_number]
        elif (row == 5): return self.row_6[column_number]
        elif (row == 6): return self.row_7[column_number]
        elif (row == 7): return self.row_8[column_number]
        else: return "error"
        print('no status returned')

    #setters
    def set_status(self, column, row, piece):
        #define column_letter
        column_letter = ''
        if (column == 0): column_letter = 'a'
        elif (column  == 1): column_letter = 'b'
        elif (column  == 2): column_letter = 'c'
        elif (column  == 3): column_letter = 'd'
        elif (column  == 4): column_letter = 'e'
        elif (column  == 5): column_letter = 'f'
        elif (column  == 6): column_letter = 'g'
        elif (column  == 7): column_letter = 'h'
        print('column is: ',column)
        print('column_letter is: ',column_letter)
        #set values
        if (row == 1): self.row_1[column] = column_letter+'_'+'1'+'_'+piece
        elif (row == 2): self.row_2[column] = column_letter+'_'+'2'+'_'+piece
        elif (row == 3): self.row_3[column] = column_letter+'_'+'3'+'_'+piece
        elif (row == 4): self.row_4[column] = column_letter+'_'+'4'+'_'+piece
        elif (row == 5): self.row_5[column] = column_letter+'_'+'5'+'_'+piece
        elif (row == 6): self.row_6[column] = column_letter+'_'+'6'+'_'+piece
        elif (row == 7): self.row_7[column] = column_letter+'_'+'7'+'_'+piece
        elif (row == 8): self.row_8[column] = column_letter+'_'+'8'+'_'+piece
        else: return "error"

    #print the board to the console
    def display(self):
        #for every element in each row, print the correspodning chess piece from assets
        for i in range(8):
            tempRow = []
            for x in self.board[i]:
                space_info = x.split('_')
                piece_info = space_info[-2]+'_'+space_info[-1]
                piece = assets.assets.get_piece(piece_info)
                if (space_info[-1] == 'empty'): tempRow.append("""
____
|  |
|  |
|  |
|__|
                """)
                else: tempRow.append(piece)
            #displaying the board
            #implemented from a kind soul on stackoverflow: 
            #https://stackoverflow.com/questions/43372078/how-to-print-multiline-strings-on-the-same-line-in-python
            #thank you Vield for your useful code
            strings_by_column = [s.split('\n') for s in tempRow]
            strings_by_line = zip(*strings_by_column)
            max_length_by_column = [
                max([len(s) for s in col_strings])
                for col_strings in strings_by_column
            ]
            for parts in strings_by_line:
                padded_strings = [
                    parts[i].ljust(max_length_by_column[i])
                    for i in range(len(parts))
                ]
                print(''.join(padded_strings))

        #looking at matrice for testing purposes
        for x in self.board: print(x)
    #check if a piece is present on the board
    def check_presence(self, row, col):
        try:
            col_letter = moves.get_col_letter(col)
            #print('checking presence... row is '+str(row)+' col is '+str(col_letter))
            space = ''
            tempRow = self.board[row]
            #print('tempRow is ', tempRow)
            for x in tempRow:
                if(x[0] == col_letter): 
                    space = x
                    #print('if statement triggered: space is:',x)
            space_info = space.split('_')
            if (space_info[-1] != 'empty'): return True
            else: return False
        except IndexError: return True

    #save the board as a text file
    def save(filename):
        f = open(filename, 'a')
        for x in baord.board:
            f.write(x)
        f.close()
        print('game saved')