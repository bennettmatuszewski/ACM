import random
from bs4 import BeautifulSoup
import requests

def quote_guessing_game():
    print("Welcome to the Web Scraping Quote Game!")
    print("I'll scrape a random quote, and you try to guess the author.")
    
    #Get quotes from a quotes website
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #Find all quotes and authors on the page
    quote_elements = soup.find_all('div', class_='quote')
    
    score = 0
    total_questions = 5
    
    for i in range(total_questions):
        # elect a random quote
        random_quote = random.choice(quote_elements)
        
        #Extract the quote text and author
        quote_text = random_quote.find('span', class_='text').text
        author = random_quote.find('small', class_='author').text
        
        #Show the quote and ask for guess
        print(f"\nQuestion {i+1}/{total_questions}")
        print(f"Quote: {quote_text}")
        guess = input("Who wrote this quote? ")
        
        #Check the answer
        if guess.lower() == author.lower():
            print("Correct! Well done!")
            score += 1
        else:
            print(f"Sorry, the author was {author}")
    
    print(f"\nGame over! Your final score: {score}/{total_questions}")

quote_guessing_game()