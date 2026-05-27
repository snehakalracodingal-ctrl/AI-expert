import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "🎮 Welcome to Rock Paper Scissors with AI 🎮")

# Choices
choices = ["rock", "paper", "scissors"]

# Scores
player_score = 0
ai_score = 0

while True:
    print("\nChoose Rock, Paper, or Scissors")
    player = input("Your choice: ").lower()

    # Exit option
    if player == "exit":
        print(Fore.YELLOW + "\nGame Ended!")
        break

    # Invalid input
    if player not in choices:
        print(Fore.RED + "❌ Invalid choice! Try again.")
        continue

    # AI Strategy
    # AI randomly chooses, but slightly smarter
    if player == "rock":
        ai = random.choice(["paper", "rock"])
    elif player == "paper":
        ai = random.choice(["scissors", "paper"])
    else:
        ai = random.choice(["rock", "scissors"])

    print(Fore.MAGENTA + f"🤖 AI chose: {ai}")

    # Winning conditions
    if player == ai:
        print(Fore.YELLOW + "😐 It's a Tie!")

    elif (
        (player == "rock" and ai == "scissors") or
        (player == "paper" and ai == "rock") or
        (player == "scissors" and ai == "paper")
    ):
        print(Fore.GREEN + "🎉 You Win This Round!")
        player_score += 1

    else:
        print(Fore.RED + "💀 AI Wins This Round!")
        ai_score += 1

    # Scoreboard
    print(Fore.CYAN + f"\n📊 Scoreboard")
    print(Fore.GREEN + f"You: {player_score}")
    print(Fore.RED + f"AI : {ai_score}")

# Final Result
print(Fore.BLUE + "\n🏁 Final Scores")
print(Fore.GREEN + f"You: {player_score}")
print(Fore.RED + f"AI : {ai_score}")

if player_score > ai_score:
    print(Fore.GREEN + "🔥 Congratulations! You defeated the AI.")
elif ai_score > player_score:
    print(Fore.RED + "🤖 AI dominated the game.")
else:
    print(Fore.YELLOW + "⚔️ The battle ended in a draw.")