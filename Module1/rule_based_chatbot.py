import random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beach": ["Bali", "Maldives"],
    "mountain": ["Himalayas", "Swiss Alps"],
    "city": ["Paris", "Tokyo"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? It had a virus!"
]

def recommend():
    choice = input(Fore.CYAN + "Beach, mountain, or city? ").lower()

    if choice in destinations:
        place = random.choice(destinations[choice])
        print(Fore.GREEN + f"Try visiting {place}!")
    else:
        print(Fore.RED + "Sorry, no suggestion available.")

def packing():
    days = input(Fore.CYAN + "How many days are you traveling? ")
    print(Fore.GREEN + f"Pack clothes, charger, and essentials for {days} days.")

def joke():
    print(Fore.YELLOW + random.choice(jokes))

print(Fore.CYAN + "Welcome to TravelBot!")

while True:
    user = input(Fore.MAGENTA + "\nType recommend / packing / joke / exit: ").lower()

    if user == "recommend":
        recommend()

    elif user == "packing":
        packing()

    elif user == "joke":
        joke()

    elif user == "exit":
        print(Fore.CYAN + "Goodbye! Safe travels ✈️")
        break

    else:
        print(Fore.RED + "Invalid choice!")