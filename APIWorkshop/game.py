#pip insstall countryinfo

from countryinfo import CountryInfo
import random

gameCountries = list(CountryInfo().all())

def get_random_country(gameCountries):
    return random.choice(gameCountries)

def play_game():
    print("Welcome to capital guesser!")
    streak = 0
    while True:
        selectedCountry = get_random_country(gameCountries)
        capital = CountryInfo(selectedCountry).capital()
        
        print(f"What is the capital of {selectedCountry}?")
        player_guess = input()

        if player_guess.lower() == capital.lower():
            streak += 1
            print(f"Correct! Your streak is {streak}.\n")
        else:
            print(f"Incorrect. The correct answer is {capital}.\n")
            print(f"Your final streak is {streak}.")
            break

play_game()




