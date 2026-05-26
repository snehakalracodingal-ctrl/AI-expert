import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Travel destinations
destinations = {
    "beach": ["Bali", "Maldives", "Phuket"],
    "mountain": ["Himalayas", "Swiss Alps", "Rocky Mountains"],
    "city": ["Paris", "Tokyo", "New York"]
}

# Jokes list
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "Why do travelers love WiFi? Because connection matters!"
]

# Recommend places
def recommend():
    choice = input(Fore.CYAN + "Beach, mountain, or city? ").lower()

    if choice in destinations:
        place = random.choice(destinations[choice])
        print(Fore.GREEN + f"You should visit {place}!")
    else:
        print(Fore.RED + "Sorry, destination not available.")

# Packing tips
def packing():
    days = input(Fore.CYAN + "How many days are you traveling? ")

    print(Fore.GREEN + f"\nPacking tips for {days} days:")
    print(Fore.GREEN + "- Pack comfortable clothes")
    print(Fore.GREEN + "- Carry charger and power bank")
    print(Fore.GREEN + "- Keep important documents")

# Tell jokes
def joke():
    print(Fore.YELLOW + random.choice(jokes))

# Weather feature
def weather():
    city = input(Fore.CYAN + "Enter city name: ")
    print(Fore.GREEN + f"The weather in {city} is sunny and 28°C.")

# News feature
def news():
    print(Fore.YELLOW + "\nTravel News:")
    print(Fore.GREEN + "- Summer travel discounts available.")
    print(Fore.GREEN + "- New international flights launched.")
    print(Fore.GREEN + "- Tourism is increasing worldwide.")

# Local time feature
def local_time():
    city = input(Fore.CYAN + "Enter city name: ").lower()

    times = {
        "paris": "10:00 AM",
        "tokyo": "6:00 PM",
        "new york": "4:00 AM",
        "delhi": "2:30 PM"
    }

    if city in times:
        print(Fore.GREEN + f"Local time in {city.title()} is {times[city]}")
    else:
        print(Fore.RED + "Sorry, time data not available.")

# Main chatbot
print(Fore.CYAN + "🌍 Welcome to TravelBot ✈️")

name = input(Fore.YELLOW + "Enter your name: ")

print(Fore.GREEN + f"Hello {name}! Nice to meet you.\n")

while True:

    print(Fore.MAGENTA + "\nChoose an option:")
    print("recommend / packing / joke / weather / news / time / exit")

    user = input(Fore.YELLOW + f"{name}: ").lower()

    if user == "recommend":
        recommend()

    elif user == "packing":
        packing()

    elif user == "joke":
        joke()

    elif user == "weather":
        weather()

    elif user == "news":
        news()

    elif user == "time":
        local_time()

    elif user == "exit":
        print(Fore.CYAN + "Goodbye! Safe travels ✈️")
        break

    else:
        print(Fore.RED + "Invalid option! Try again.")