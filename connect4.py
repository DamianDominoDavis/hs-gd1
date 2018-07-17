from random import randint, choice

def accept_nums(prompt, l, valids, delim=' '):
	while True:
		try:
			n = [int(x) for x in input(prompt + " ").split(delim)]
			m = [e for e in n if e in valids]
			if len(m) == l and n == m:
				break
		except:
			pass
	return n

def print_board(board):
	for col in board[::-1]:
		for i in range(len(col)):
			print(''.join(str(board[col][-i])))
			i += 1

def drop(col, symbol):
	for i in range(len(col)):
		if col[i] == None:
			break
		i += 1
	col[i] = symbol

def over():
	full = True
	for col in board:
		if None in col:
			full = False
			break
	return full


if __name__ == '__main__':
	board = [[None for y in range(6)] for x in range(7)]
	rules = '''Connect 4'''
	print(rules, "\n")
	mine, thine = ['X','O'] if choice([True, False]) else ['O','X']
	myturn = mine == 'X'
	while not over():
		print_board(board)
		if myturn:
			n = board[accept_nums("Play column 0-7?", 1, list(range(0,7)))[0]]
		else:
			n = choice([col for col in board if None in col])
		if None in n:
			drop(n, mine if myturn else thine)
			myturn = not myturn
	print_board(board)
	