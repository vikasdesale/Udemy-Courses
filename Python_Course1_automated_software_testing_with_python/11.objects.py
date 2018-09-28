lottery_player_dict = {
	'name': 'Rolf',
	'numbers': (5, 9, 12, 3, 1, 21)
}

class lotteryPlayer:
	def __init__(self, name):
		self.name = name
		self.numbers = {5, 9, 12, 3, 1, 21}

	def total(self):
		return sum(self.numbers)

player_one = lotteryPlayer("John")
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = lotteryPlayer("Rolf")

print(player_one.numbers == player_two.numbers)

