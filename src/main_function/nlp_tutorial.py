import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher
from src.utils.support_functions.support_functions import flatten_list
from collections import Counter
nlp = spacy.load('en_core_web_sm')

# Creates Token


data = pd.read_json(
    'C:/Users/Robert/Documents/Projekte/dev/nlp_tool/data/yelp_reviews/restaurant.json', encoding='utf8')['restaurants']

#Exercise to find Lemmas
if True:
    # Create List to save lemma of ratings
    ratings_lemma = dict()
    ratings_common = dict()
    for r in range(0, 6):
        ratings_lemma[str(r)] = []
        ratings_common[str(r)] = []

    # Iterate every restaurant
    for restaurant in data:
        # itereate everey revies
        for review in restaurant['reviews']:
            # Get Text
            doc = nlp(review['comments'])
            # Get token
            lemma = [token.lemma_ for token in doc]
            # Save Text to Rating
            ratings_lemma[str(review['rating'])].append(lemma)

    drop_list = ['I','.','a','be','for','and',',','the','of','to']
    for ratings in ratings_lemma:
        # Unlist Comments
        ratings_lemma[ratings] = flatten_list(ratings_lemma[ratings])
        # Save most common expression
        ratings_common[ratings] = Counter(ratings_lemma[ratings]).most_common(20)
        print(ratings_common[ratings])

    print('End')

#Exercise to find patterns
if True:
    # List to create Patterns with
    menu = ["Cheese Steak", "Cheesesteak", "Steak and Cheese", "Italian Combo", "Tiramisu", "Cannoli",
            "Chicken Salad", "Chicken Spinach Salad", "Meatball", "Pizza", "Pizzas", "Spaghetti",
            "Bruchetta", "Eggplant", "Italian Beef", "Purista", "Pasta", "Calzones",  "Calzone",
            "Italian Sausage", "Chicken Cutlet", "Chicken Parm", "Chicken Parmesan", "Gnocchi",
            "Chicken Pesto", "Turkey Sandwich", "Turkey Breast", "Ziti", "Portobello", "Reuben",
            "Mozzarella Caprese",  "Corned Beef", "Garlic Bread", "Pastrami", "Roast Beef",
            "Tuna Salad", "Lasagna", "Artichoke Salad", "Fettuccini Alfredo", "Chicken Parmigiana",
            "Grilled Veggie", "Grilled Veggies", "Grilled Vegetable", "Mac and Cheese", "Macaroni",  
            "Prosciutto", "Salami", "Tacos"]

    matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
    #Create Patterns
    patterns = [nlp(text) for text in menu]
    #Add list with patterns
    matcher.add("Menu-List", patterns)

    # Iterate over all restaurants
    for restaurant in data:
        # itereate everey revies
        for review in restaurant['reviews']:
            # Get Comments
            comments = review['comments']
            #Check
            nlp_review = nlp(comments)
            # Find Matches
            matches = matcher(nlp_review)
            print(matches)
            try:
                for match in matches:
                    match_id, start, end = match
                    print(nlp.vocab.strings[match_id], nlp_review[start:end])
            except:
                print('Fehler')
                pass
print('End')

#Example
if False:
    # Text preprocessing
    # print table with lemma of token and wether it is a stopword
    # lemma = Wortstamm
    print("\n Start Text Preprocessing")
    print(f"Token \t\t\tLemma \t\t\tStopword".format(
        'Token', 'Lemma', 'Stopword'))
    print("-"*60)
    for token in doc:
        print(f"{str(token)}\t\t\t{token.lemma_}\t\t\t{token.is_stop}")
if False:
    # Pattern Matching
    print("\n Start Pattern Matching")
    matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
    terms = ['Galaxy Note', 'iPhone 11', 'iPhone XS', 'Google Pixel']
    # Creates Tokens to  every text
    patterns = [nlp(text) for text in terms]
    matcher.add("Mobile Phone List", patterns)
    # Borrowed from https://daringfireball.net/linked/2019/09/21/patel-11-pro

    # Create Tokes to every Text
    text_doc = nlp("Glowing review overall, and some really interesting side-by-side "
                   "photography tests pitting the iPhone 11 Pro against the "
                   "Galaxy Note 10 Plus and last year’s iPhone XS and Google Pixel 3.")
    # positions of the start and end of the phrase
    matches = matcher(text_doc)
    print(matches)

    match_id, start, end = matches[0]
    print(nlp.vocab.strings[match_id], text_doc[start:end])
