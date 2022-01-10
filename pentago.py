import numpy as np

def display_board(board):
    print(board)
    pass

def win_board(board): #func to check win at any instance
    p1win = False
    p2win = False
    #horizontal
    for r in range(6):
        for c in range(2):
            if board[r,c] == board[r,c+1] == board[r,c+2] == board[r,c+3] == board[r,c+4]:
                if board[r,c] == 1: p1win = True
                elif board[r,c] == 2: p2win = True
    #vertical
    for c in range(6):
        for r in range(2):
            if board[r,c] == board[r+1,c] == board[r+2,c] == board[r+3,c] == board[r+4,c]:
                if board[r,c] == 1: p1win = True
                elif board[r,c] == 2: p2win = True
    #diagonal negative slope
    for c in range(2):
        for r in range(2):
            if board[r,c] == board[r+1,c+1] == board[r+2,c+2] == board[r+3,c+3] == board[r+4,c+4]:
                if board[r,c] == 1: p1win = True
                elif board[r,c] == 2: p2win = True
    #diagonal postive slope
    for c in range(2):
        for r in range(4,6):
            if board[r,c] == board[r-1,c+1] == board[r-2,c+2] == board[r-3,c+3] == board[r-4,c+4]:
                if board[r,c] == 1: p1win = True
                elif board[r,c] == 2: p2win = True
                
    if p1win is True and p2win is False: return 1 #P1 wins
    elif p2win is True and p1win is False: return 2 #P2 wins
    elif p1win is True and p2win is True: return 3 #Both win: Draw

def rotate_board(board,direction,rot):
    copy = np.copy(board)
    #split board into four 3x3 quadrants clockwise from top right
    quad1 = copy[0:3,3:6] #top right
    quad2 = copy[3:6,3:6] #bottom right
    quad3 = copy[3:6,0:3] #bottom left
    quad4 = copy[0:3,0:3] #top left
    
    if direction == 1: #user specified rot
        if rot == 1:
            quad1 = np.rot90(quad1,3) #rot clockwise
        elif rot == 2:
            quad1 = np.rot90(quad1) #rot anticlockwise
        elif rot == 3:
            quad2 = np.rot90(quad2,3)
        elif rot == 4:
            quad2 = np.rot90(quad2)
        elif rot == 5:
            quad3 = np.rot90(quad3,3)
        elif rot == 6:
            quad3 = np.rot90(quad3)
        elif rot == 7:
            quad4 = np.rot90(quad4,3)
        elif rot == 8:
            quad4 = np.rot90(quad4) 
        left = np.vstack((quad4,quad3)) #recombine left half of board
        right = np.vstack((quad1,quad2)) #recombine right half of board
        copy = np.hstack((left,right)) #recombine full board
        return copy
    
    elif direction == 2: #anti rotation 
        if rot == 1:
            quad1 = np.rot90(quad1) #rot anticlockwise
        elif rot == 2:
            quad1 = np.rot90(quad1,3) #rot clockwise
        elif rot == 3:
            quad2 = np.rot90(quad2)
        elif rot == 4:
            quad2 = np.rot90(quad2,3)
        elif rot == 5:
            quad3 = np.rot90(quad3)
        elif rot == 6:
            quad3 = np.rot90(quad3,3)
        elif rot == 7:
            quad4 = np.rot90(quad4)
        elif rot == 8:
            quad4 = np.rot90(quad4,3)
        left = np.vstack((quad4,quad3)) 
        right = np.vstack((quad1,quad2))
        copy = np.hstack((left,right))
        return copy

def check_victory(board,turn,rot):
    beforerot = rotate_board(board,2,rot) #board before rotation
    if win_board(beforerot) == 1: return 1 #P1 wins before rot
    elif win_board(beforerot) == 2: return 2 #P2 wins before rot
    elif win_board(board) == 1: return 1 #P1 wins after rot
    elif win_board(board) == 2: return 2 #P2 wins after rot
    elif win_board(board) == 3: return 3 #Both win: Draw
    elif 0 not in board: return 3 #board full: Draw
    else: return 0
    
def apply_move(board,turn,row,col,rot):
    copy = np.copy(board)
    copy[row,col] = turn #apply piece 1 or 2
    copy = rotate_board(copy,1,rot)
    return copy

def check_move(board,row,col):
    if board[row,col] == 0:    
        return True
    else:
        return False

def randmove(board):
    import random
    while True:
        row = random.randint(0,5)
        col = random.randint(0,5)
        rot = random.randint(1,8)
        if check_move(board,row,col) is True: #if illegalmove, get new numbers
            print(row,col,rot) ##########################
            return (row,col,rot)

def computer_move(board,turn,level):
    import random
    if level == 1:
        return randmove(board)
            
    elif level == 2:   #?????? define testing func, np.apply_along_axis
        copy1 = np.copy(board)
        goodmoves = [] #list of goodmoves that block human win
        class badmove(Exception): pass #error to break out of 3 loops
        if np.count_nonzero(copy1) >= 7:
            for row in range(0,6):
                for col in range(0,6):
                    for rot in range(1,9):
                        if check_move(copy1,row,col) is True:
                            copy2 = apply_move(copy1,turn,row,col,rot)
                            if check_victory(copy2,turn,rot) == turn:
                                print('win le',row,col,rot) ################
                                return row,col,rot
                            elif check_victory(copy2,turn,rot) == 3:
                                print('draw le',row,col,rot) ###############
                                return row,col,rot
                            else:
                                try:
                                    for rot2 in range(1,9):     
                                        for row2 in range(0,6):
                                            for col2 in range(0,6):
                                                if check_move(copy2,row2,col2) is True:
                                                    copy3 = apply_move(copy2,1,row2,col2,rot2)
                                                    if check_victory(copy3,turn,rot2) == 1:
                                                        raise badmove
                                except badmove: pass
                                else: 
                                    goodmoves.append((row,col,rot))
                                finally: 
                                    copy2 = np.copy(copy1)
                                    copy3 = np.copy(copy1)        
        try:
            move = random.choice(goodmoves) #randomly choose move from list
            print('from',goodmoves) ###########################
            print(move) ##########################
            return move
        except:
            print('rand cause <7 or confirm lose') ##########################
            return randmove(board)
                
def menu():  
    print('\nWelcome to Pentago')  
    game_board = np.zeros((6,6)) 
    game_over = False
    turn = 1
    mode = 0

    class RotOutOfBounds(Exception): pass #when rot not 1 to 8
    class SpaceFilled(Exception): pass #when position alr occupied
        
    while mode != '1' and mode != '2':
        mode = input('Enter 1 for PvP, 2 to vs Computer:')
                           
    if mode == '1':
        print('PvP mode selected')
        display_board(game_board)
        while not game_over:
            print('Player',turn,'turn')
            try:
                row = int(input('row 0-5?'))
                col = int(input('col 0-5?'))
                rot = int(input('rot 1-8?'))
                if check_move(game_board,row,col) is False:
                    raise SpaceFilled
                elif rot not in range(1,9):
                    raise RotOutOfBounds  
                else:
                    game_board = apply_move(game_board,turn,row,col,rot)
                    display_board(game_board)                       
                    if check_victory(game_board,turn,rot) == 1:
                        print('P1 wins!','Game over')
                        game_over = True
                    elif check_victory(game_board,turn,rot) == 2:
                        print('P2 wins!','Game over')
                        game_over = True
                    elif check_victory(game_board,turn,rot) == 3:
                        print('DRAW!','Game over')
                        game_over = True
                    else:
                        print('')
                        if turn == 1: 
                            turn = 2
                        elif turn == 2: 
                            turn = 1
            except SpaceFilled:
                print('Position already occupied')
            except RotOutOfBounds:
                print('Invalid rotation')
            except:
                print('Invalid input')
                        
    elif mode == '2':
        print('Computer mode selected')
        display_board(game_board)
        while True:
            try:
                level = int(input('Computer level 1 or 2:'))
                if level != 1 and level != 2:
                    raise Exception
                else: break
            except:
                print('enter level 1 or 2')
                
        while not game_over:
            if turn == 1:
                print('Human turn',end='')
                try:
                    row = int(input('row 0-5?'))
                    col = int(input('col 0-5?'))
                    rot = int(input('rot 1-8?'))
                    if check_move(game_board,row,col) is False:
                        raise SpaceFilled
                    elif rot not in range(1,9):
                        raise RotOutOfBounds  
                    else:
                        game_board = apply_move(game_board,turn,row,col,rot)
                        print('\nYour move:')
                        display_board(game_board)                       
                        if check_victory(game_board,turn,rot) == 1:
                            print('P1 wins!','Game over')
                            game_over = True
                        elif check_victory(game_board,turn,rot) == 2:
                            print('CPU wins!','Game over')
                            game_over = True
                        elif check_victory(game_board,turn,rot) == 3:
                            print('DRAW!','Game over')
                            game_over = True
                        else:
                            turn = 2
                except SpaceFilled:
                    print('Position already occupied')
                except RotOutOfBounds:
                    print('Invalid rotation')
                except:
                    print('Invalid input')
                    
            elif turn == 2:
                print("\nCPU's move:")
                row,col,rot = computer_move(game_board,turn,level)
                game_board = apply_move(game_board,turn,row,col,rot)
                display_board(game_board)
                print('')
                if check_victory(game_board,turn,rot) == 1:
                    print('P1 wins!','Game over')
                    game_over = True
                elif check_victory(game_board,turn,rot) == 2:
                    print('CPU wins!','Game over')
                    game_over = True
                elif check_victory(game_board,turn,rot) == 3:
                    print('DRAW!','Game over')
                    game_over = True
                else:
                    turn = 1

menu()










