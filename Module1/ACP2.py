import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama
colorama.init()

# Welcome Message
print(f"{Fore.CYAN}🐍 Welcome to Sentiment Spy: Mission Report 🐍{Style.RESET_ALL}")

# User Name
user_name = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}")

# Lists and Counters
history = []

positive_count = 0
negative_count = 0
neutral_count = 0

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Main Chat Loop
while True:

    user_input = input(f"\n{Fore.YELLOW}You: {Style.RESET_ALL}")

    # Convert command to lowercase
    command = user_input.lower()

    # EXIT COMMAND
    if command == "exit":
        print(f"\n{Fore.CYAN}📋 Final Mission Report 📋{Style.RESET_ALL}")

        print(f"User Name      : {user_name}")
        print(f"Total Messages : {len(history)}")
        print(f"Positive Count : {positive_count}")
        print(f"Negative Count : {negative_count}")
        print(f"Neutral Count  : {neutral_count}")

        print(f"\n{Fore.GREEN}Thanks for using Sentiment Spy! 🚀{Style.RESET_ALL}")
        break

    # HISTORY COMMAND
    elif command == "history":
        print(f"\n{Fore.BLUE}📝 Conversation History 📝{Style.RESET_ALL}")

        if len(history) == 0:
            print("No history available.")
        else:
            for item in history:
                print(item)

    # STATS COMMAND
    elif command == "stats":
        print(f"\n{Fore.GREEN}📊 Sentiment Statistics 📊{Style.RESET_ALL}")
        print(f"Positive : {positive_count}")
        print(f"Negative : {negative_count}")
        print(f"Neutral  : {neutral_count}")

    # RESET COMMAND
    elif command == "reset":
        history.clear()

        positive_count = 0
        negative_count = 0
        neutral_count = 0

        print(f"{Fore.RED}All data has been reset! 🔄{Style.RESET_ALL}")

    # SENTIMENT ANALYSIS
    else:
        result = analyze_sentiment(user_input)

        # Store history
        history.append(f"You: {user_input} --> {result}")

        # Update counts
        if "Positive" in result:
            positive_count += 1
        elif "Negative" in result:
            negative_count += 1
        else:
            neutral_count += 1

        # Display Result
        print(f"{Fore.CYAN}Sentiment:{Style.RESET_ALL} {result}")