import random

choices = ['stone', 'paper', 'scissor']
win_map = {'stone': 'scissor', 'paper': 'stone', 'scissor': 'paper'}
user_history = []

def ai_choice(user_history):
	if not user_history:
		return random.choice(choices)
	# Predict the user's next move as their most frequent previous move
	predicted = max(set(user_history), key=user_history.count)
	# AI picks the move that beats the predicted move
	for move, beats in win_map.items():
		if beats == predicted:
			return move
	return random.choice(choices)

print("Welcome to Hard Stone Paper Scissor Game!")
rounds = 5
user_score = 0
computer_score = 0

for i in range(rounds):
	print(f"\nRound {i+1} of {rounds}")
	user_choice = input("Enter your choice (stone, paper, scissor): ").lower()
	if user_choice not in choices:
		print("Invalid choice! Please choose stone, paper, or scissor.")
		continue
	computer_choice = ai_choice(user_history)
	print(f"Computer chose: {computer_choice}")
	user_history.append(user_choice)
	if user_choice == computer_choice:
		print("It's a tie!")
	elif (
		(user_choice == 'stone' and computer_choice == 'scissor') or
		(user_choice == 'paper' and computer_choice == 'stone') or
		(user_choice == 'scissor' and computer_choice == 'paper')
	):
		print("You win this round!")
		user_score += 1
	else:
		print("Computer wins this round!")
		computer_score += 1

print(f"\nFinal Score: You {user_score} - Computer {computer_score}")
if user_score > computer_score:
	print("Congratulations! You win the game!")
elif user_score < computer_score:
	print("Computer wins the game! Better luck next time.")
else:
	print("It's a draw!")
