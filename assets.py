
#class with text art for each chess piece 
class assets:
    #pieces text art
    white_pawn = """

 o              
 U              
[_]             
WwW             
    """
    white_rook = """

L-|             
 U              
[_]             
WwW             
    """
    white_knight = """

/')             
 U              
[_]             
WwW             
    """
    white_bishop = """

(\)             
 U              
[_]             
WwW             
    """
    white_king = """
 +              
) (             
) (             
[_]             
WwW             
    """
    white_queen = """
 .              
) (             
) (             
[_]             
WwW             
    """
    black_pawn = """

 o              
 U              
[_]             
BbB             
    """
    black_rook = """

L-|             
 U              
[_]             
BbB             
    """
    black_knight = """

/')             
 U              
[_]             
BbB             
    """
    black_bishop = """
            
(\)             
 U              
[_]             
BbB             
    """
    black_king = """
 +              
) (             
) (             
[_]             
BbB             
    """
    black_queen = """
 .              
) (             
) (             
[_]             
BbB             
    """

    #getters
    def get_piece(name):
        if (name == 'pawn_white'): return assets.white_pawn
        elif (name == 'rook_white'): return assets.white_rook
        elif (name == 'knight_white'): return assets.white_knight
        elif (name == 'bishop_white'): return assets.white_bishop
        elif (name == 'king_white'): return assets.white_king
        elif (name == 'queen_white'): return assets.white_queen
        elif (name == 'pawn_black'): return assets.black_pawn
        elif (name == 'rook_black'): return assets.black_rook
        elif (name == 'knight_black'): return assets.black_knight
        elif (name == 'bishop_black'): return assets.black_bishop
        elif (name == 'king_black'): return assets.black_king
        elif (name == 'queen_black'): return assets.black_queen
        else: return "error"