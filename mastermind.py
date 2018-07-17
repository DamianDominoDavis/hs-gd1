from random import randint

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

if __name__ == '__main__':
	target = [randint(0,6) for x in range(0,4)]
	rules = '''Welcome to Mastermind!

The object of the game is to win. I know a four-digit code of numbers 0-6;
you guess a number, and I'll tell you how many digits are in the correct answer.
I'll even tell you how many are in the right spot!
'''
	print(rules)
	turns = 10
	while True:
		print(turns, "guesses left.")
		guess = accept_nums("Guess four digits 0-6, with spaces:", 4, list(range(0,7)))
		red, white = 0, 0
		extra = []
		for i in range(0,4):
			if guess[i] == target[i]:
				red += 1
			else:
				extra.append(guess[i])
		if red == 4:
			break
		check = target.copy()
		for x in extra:
			if x in check:
				extra.remove(x)
				check.remove(x)
				white += 1
		print(white, "digits almost right, and ", red, "perfect.")
		turns -= 1
		if turns == 0:
			break
	print("You", "win!" if red == 4 else "lose. The correct answer was", ' '.join([str(x) for x in target]))
	exit()
