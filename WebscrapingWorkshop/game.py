#pip install requests
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import random

def get_random_professor_url(filename="Webscraping-Workshop/professor_ids.txt"):
    with open(filename, "r") as file:
        professor_ids = [line.strip() for line in file if line.strip()]
    
    random_professor_id = random.choice(professor_ids)
    url = f"https://www.ratemyprofessors.com/professor/{random_professor_id}"
    return url

url = get_random_professor_url()
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

reviews = soup.find_all("div", class_='Rating__RatingBody-sc-1rhvpxz-0')
reviewComments = []
reviewRatings = []

for review in reviews:
    reviewComments.append(review.find("div", class_="Comments__StyledComments-dzzyvm-0").string)
    reviewRatings.append(review.find("div", class_="CardNumRating__CardNumRatingNumber-sc-17t4b9u-2").string)

def calculate_score(actual, guess):
    difference = abs(actual - guess)
    if difference == 0:
        return 10
    elif difference <= 1:
        return 7
    elif difference <= 2:
        return 5
    elif difference <= 3:
        return 3
    else:
        return 0 

def play_game():
    score = 0
    rounds = 5
    
    for _ in range(rounds):
        index = random.randint(0, len(reviewComments) - 1)
        comment = reviewComments.pop(index)
        actual_rating = reviewRatings.pop(index)
        
        print(f"Comment: {comment} \n")
        guess = int(input("Guess the rating (1-5): "))
        round_score = calculate_score(int(actual_rating[0]), guess)
        score += round_score
        
        print(f"Actual Rating: {actual_rating}")
        print(f"You earned {round_score} points. Total Score: {score}\n")
    
    print(f"Game Over! Final Score: {score}")

play_game()
