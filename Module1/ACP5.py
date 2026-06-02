

import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Load Dataset
try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: 'imdb_top_1000.csv' not found!")
    raise SystemExit

# Get All Genres
genres = sorted({
    g.strip()
    for genre_list in df["Genre"].dropna().str.split(", ")
    for g in genre_list
})

# Loading Animation
def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
    print()

# Convert Polarity to Sentiment
def senti(p):
    if p > 0:
        return "Positive 😊"
    elif p < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Recommendation Function
def recommend(genre=None, mood=None, rating=None, n=5):

    data = df.copy()

    # Genre Filter
    if genre:
        data = data[data["Genre"].str.contains(genre, case=False, na=False)]

    # Rating Filter
    if rating is not None:
        data = data[data["IMDB_Rating"] >= rating]

    if data.empty:
        return "No suitable movie recommendations found."

    # Random Shuffle
    data = data.sample(frac=1).reset_index(drop=True)

    recommendations = []

    for _, row in data.iterrows():

        overview = row.get("Overview")

        if pd.isna(overview):
            continue

        polarity = TextBlob(str(overview)).sentiment.polarity

        recommendations.append({
            "Title": row["Series_Title"],
            "Genre": row["Genre"],
            "Rating": row["IMDB_Rating"],
            "Overview": overview,
            "Polarity": polarity,
            "Sentiment": senti(polarity)
        })

        if len(recommendations) == n:
            break

    return recommendations if recommendations else "No suitable movie recommendations found."

# Display Recommendations
def show(recs, name):

    print(Fore.YELLOW + f"\n🍿 Movie Recommendations For {name}\n")

    for i, movie in enumerate(recs, 1):

        print(Fore.CYAN + "=" * 70)
        print(Fore.GREEN + f"{i}. 🎥 {movie['Title']}")
        print(Fore.WHITE + f"Genre       : {movie['Genre']}")
        print(Fore.WHITE + f"IMDB Rating : {movie['Rating']}")
        print(Fore.WHITE + f"Sentiment   : {movie['Sentiment']}")
        print(Fore.WHITE + f"Polarity    : {movie['Polarity']:.2f}")
        print(Fore.WHITE + f"Overview    : {movie['Overview']}")
        print(Fore.CYAN + "=" * 70)

# Genre Selection
def get_genre():

    print(Fore.GREEN + "\nAvailable Genres:\n")

    for i, g in enumerate(genres, 1):
        print(Fore.CYAN + f"{i}. {g}")

    while True:

        choice = input(
            Fore.YELLOW +
            "\nEnter Genre Number or Genre Name: "
        ).strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(genres):
                return genres[choice - 1]

        choice = choice.title()

        if choice in genres:
            return choice

        print(Fore.RED + "Invalid Genre! Try Again.")

# Rating Selection
def get_rating():

    while True:

        value = input(
            Fore.YELLOW +
            "\nEnter Minimum IMDB Rating (7.6 - 9.3) or 'skip': "
        ).strip()

        if value.lower() == "skip":
            return None

        try:

            rating = float(value)

            if 7.6 <= rating <= 9.3:
                return rating

            print(Fore.RED + "Rating must be between 7.6 and 9.3")

        except ValueError:
            print(Fore.RED + "Invalid Input!")

# Main Program
print(Fore.BLUE + "\n🎬 AI Movie Recommendation System 🎬\n")

name = input(Fore.YELLOW + "Enter Your Name: ")

print(Fore.GREEN + f"\nWelcome, {name}! 😊")

# Recommendation Type
print(Fore.BLUE + "\nChoose Recommendation Type")
print(Fore.CYAN + "1. Genre Based Recommendation")
print(Fore.CYAN + "2. Random Recommendation")

choice = input(Fore.YELLOW + "\nEnter Choice (1/2): ")

if choice == "1":
    genre = get_genre()
else:
    genre = None

# Mood Input
mood = input(
    Fore.YELLOW +
    "\nHow are you feeling today? "
)

print(Fore.BLUE + "\nAnalyzing Mood", end="")
dots()

mood_polarity = TextBlob(mood).sentiment.polarity

if mood_polarity > 0:
    mood_type = "Positive 😊"
    print(Fore.GREEN +
          f"Your Mood: {mood_type} (Polarity: {mood_polarity:.2f})")
    print(Fore.GREEN +
          "AI Suggestion: Uplifting and inspiring movies.\n")

elif mood_polarity < 0:
    mood_type = "Negative 😞"
    print(Fore.RED +
          f"Your Mood: {mood_type} (Polarity: {mood_polarity:.2f})")
    print(Fore.RED +
          "AI Suggestion: Feel-good and motivational movies.\n")

else:
    mood_type = "Neutral 😐"
    print(Fore.BLUE +
          f"Your Mood: {mood_type} (Polarity: {mood_polarity:.2f})")
    print(Fore.BLUE +
          "AI Suggestion: Balanced movie recommendations.\n")

# Rating Filter
rating = get_rating()

print(Fore.BLUE + "\nFinding Movies", end="")
dots()

recommendations = recommend(
    genre=genre,
    mood=mood,
    rating=rating,
    n=5
)

if isinstance(recommendations, str):
    print(Fore.RED + recommendations)
else:
    show(recommendations, name)

# More Recommendations Loop
while True:

    again = input(
        Fore.YELLOW +
        "\nWould you like more recommendations? (yes/no): "
    ).lower()

    if again == "yes":

        recommendations = recommend(
            genre=genre,
            mood=mood,
            rating=rating,
            n=5
        )

        if isinstance(recommendations, str):
            print(Fore.RED + recommendations)
        else:
            show(recommendations, name)

    elif again == "no":

        print(
            Fore.GREEN +
            f"\nEnjoy your movies, {name}! 🍿🎬"
        )
        break

    else:
        print(Fore.RED + "Please enter yes or no.")