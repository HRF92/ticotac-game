import time
import random

global board
global move
def print_board(board):
	print "The board look like this: \n"
	for i in range(3):
		print " ",
		for j in range(3):
			if board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == -1:
				print 'O',	
			elif board[i*3+j] != 0:
				print board[i*3+j]-1,
			else:
				print ' ',
			
			if j != 2:
				print " | ",
		print
		if i != 2:
			print "-----------------"
		else: 
			print 
			
def print_instruction():
	print "Please use the following cell numbers to make your move"
	print_board([2,3,4,5,6,7,8,9,10])

def get_input():
	valid = False
	while not valid:
		try:
			user = raw_input("Where would you like to place O (1-9)? ")
			user = int(user)
			if user >= 1 and user <= 9:
				return user-1
			else:
				print "That is not a valid move! Please try again.\n"
				print_instruction()
		except Exception as e:
			print user + " is not a valid move! Please try again.\n"

def know_whos_first():
    valid = False
    while not valid:
            question = raw_input("Would you like to let the computer start the game?")
                    
            if question == "yes" or question == "oui":
                return 1
            elif question == "no" or question == "non":
                return -1
            else:
                print "That is not a valid answer! answer with yes or no."

def quit_game(board,msg):
	print_board(board)
	print msg
	quit()

def change_piece(piece):
    if piece == 1: return -1
    return 1

def is_terminal(board):
    """Check if there are any empty square in the board"""
    for square in board:
        if square == 0:
            return False
    return True

def check_win(board):
    win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for each in win_cond:
        try:
            if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
                return board[each[0]-1]
        except:
            pass
    return 0

def build_tree(node, piece):
    child_nodes = []
    for index, value in enumerate(node):
        if value == 0:
            new_node = list(node)
            new_node[index] = piece
            new_node = tuple(new_node)
            if not is_terminal(new_node):
                child_nodes.append(build_tree(new_node,change_piece(piece)))
            else:
                child_nodes.append(new_node)

    if child_nodes:
        return [node,child_nodes]
    return
def computerMove(board):
    start = time.time()
    game_tree = build_tree(tuple(board),1)
    end = time.time()
    #print game_tree
    print ("time elapsed calculating ", end-start)
    computer = random.randint(1,9)-1
    while board[computer] != 0:
        computer = random.randint(1,9)-1
    board[computer] = 1
    print (board)
    return board

def alreadyAwinner(board, move):
    if move > 4:
        winner = check_win(board)
        if winner != 0:
            out = "The winner is "
            out += "X" if winner == 1 else "O"
            out += " :)"
            quit_game(board,out)
        elif move == 9:
            quit_game(board,"No winner :(")
    return board

def userMove(board):
    user = get_input()
    while board[user] != 0:
        print "Invalid move! Cell already taken. Please try again.\n"
        user = get_input()
    board[user] = -1
    return board


def main():
    
    board = []
    print_instruction()
    for i in range(9):
        board.append(0)
    print board
    win = False
    move = 0
    answer = know_whos_first()
    
    if answer == 1:
        while not win:
            computerMove(board)
            move += 1
            print_board(board)
            print move
            alreadyAwinner(board, move)
            userMove(board)
            move += 1
            print move
            print_board(board)
            alreadyAwinner(board, move)
    else:
        while not win:
            userMove(board)
            move += 1
            print_board(board)
            alreadyAwinner(board, move)
            computerMove(board)
            move += 1
            print_board(board)
            alreadyAwinner(board, move)
if __name__ == "__main__":
    main()
