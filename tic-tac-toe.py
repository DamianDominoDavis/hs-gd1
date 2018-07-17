from random import choice

def isover(board):
	for i in range(0,3):
		if (board[3*i] == board[3*i+1] == board[3*i+2]):
			return board[3*1]
		if (board[i] == board[i+3] == board[i+6]):
			return board[i]
	if (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
		return board[4]
	return False

def accept_num(prompt, valids):
	while True:
		try:
			n = int(input(prompt + ' '))
			if n in valids:
				break
		except:
			pass
	return n

def draw_board(board):
	for i in range(0,3):
		print(' | '.join([str(s) for s in board[i*3:(i+1)*3]]))
		if i < 2:
			print('-'*9)

if __name__ == '__main__':
	mine, thine = ['X', 'O'][::1 if choice((True, False)) else -1]
	myturn = mine == 'X'
	cells = list(range(0,9))
	where = list(range(0,9))
	draw_board(cells)
	while where != [] and not isover(cells):
		if myturn:
			n = accept_num("Your turn! Where to go?", (range(0,9)))
		else:
			n = choice(where)
			print("My turn! I'll go", n)
		if n in where:
			where.remove(n)
			cells[n] = mine if myturn else thine
			draw_board(cells)
			myturn = not myturn
	print("Game Over")
	print("You", "win!" if isover(cells) == mine else "lose!")
	exit()
