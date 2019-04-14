import random

gameOver = False

class Player:
	def __init__(self, playerNumber):
		self.grandTotal = 0
		self.roundTotal = 0
		self.playerNumber = playerNumber
	
	def displayGrandTotal(self):
		print("Player %s's grand total is: %d" % (self.playerNumber, self.grandTotal))
	
	def displayRoundTotal(self):
		print("Player %s's round total is: %d" % (self.playerNumber, self.roundTotal))


def roll(sides):
	num_rolled = random.randint(1,sides)
	return num_rolled

def rules():
	print("\n\n********        Dice Challenge        ********\n\n")
	print("Players will roll as many times as they wish to build their round score.")
	print("Rolling a 1  or a 6 will return the round score to zero and \nit will become the other player's turn.")
	print("The first player to reach 30 or more will be the winner.\nGood luck!\n\nPlayer 1 will start.\n\n")
	
def playerTurn(player):
	sides = 6
	rolling = True
	global gameOver

	playerNum = player.playerNumber
	player.roundTotal = 0
	
	while rolling:
		roll_again = input("Player %s: ENTER = Roll.  S = Stop turn.\n" % (player.playerNumber))
		if roll_again.lower() != "s":
			num_rolled = roll(sides)
			if num_rolled == 1 or num_rolled == 6:
				player.roundTotal = 0
				if playerNum == 1:
					playerNum = 2
				else:
					playerNum = 1
				print("Player %s has rolled a %s. It is now Player %s's turn.\n" % (player.playerNumber, num_rolled, playerNum))
				rolling = False
			else:
				player.roundTotal += num_rolled
				print("You rolled a", num_rolled)
				print("Round total:", player.roundTotal)
		else:
			player.grandTotal += player.roundTotal
			
			if player.grandTotal < 30:
				print("Grand total:", player.grandTotal)
			
				if playerNum == 1:
					playerNum = 2
				else:
					playerNum = 1
					
				print("It is now Player %s's turn.\n\n" % (playerNum))
				
				return gameOver
				
			else:
				print("\n\nPlayer %s wins!\n\n" % (playerNum))
				gameOver = True
				return gameOver
	return gameOver
	
def main():
	rules()
	
	playerOne = Player(1)
	playerTwo = Player(2)
	playerNum = 0
	
	while not gameOver:
		print("Score:    Player 1: %s    Player 2: %s" % (playerOne.grandTotal, playerTwo.grandTotal))
		if playerNum == 1:
			playerNum = 2
		else:
			playerNum = 1
			
		if playerNum == 1:
			playerTurn(playerOne)
		else:
			playerTurn(playerTwo)
	
	#playerTurn(playerOne)
	
	print("Thanks for playing!\n\n")
	
main()