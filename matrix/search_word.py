board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word="ABCCED"


def find_word_in_board(board,word):
    stored_dict=dict()
    row=len(board)
    col=len(board[0])
    print("Number of rows and col = ",row,col)
    for i in range(row):
        for j in range(col):
                        

find_word_in_board(board,word)