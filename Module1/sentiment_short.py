from colorama import Fore, Style, init
from textblob import TextBlob

init()

print(f"{Fore.CYAN}🐍 Welcome to Sentiment Spy 🐍{Style.RESET_ALL}")

name = input("Enter your name: ")

if name == "":
    name = "Agent"

print(f"Hello {name}!\nType 'exit' to quit.\n")

history = []

while True:
    text = input(f"{Fore.GREEN}>> {Style.RESET_ALL}")

    if text.lower() == "exit":
        print(f"{Fore.BLUE}Goodbye {name}! 😊{Style.RESET_ALL}")
        break

    elif text.lower() == "history":
        print(history)
        continue

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
        color = Fore.GREEN

    elif polarity < 0:
        sentiment = "Negative 😞"
        color = Fore.RED

    else:
        sentiment = "Neutral 😐"
        color = Fore.YELLOW

    history.append((text, sentiment))

    print(f"{color}{sentiment} | Polarity: {polarity:.2f}{Style.RESET_ALL}")