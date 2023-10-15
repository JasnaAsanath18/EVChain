import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')



#     # Example user reviews of charging stations
#     # reviews = [
#     #     "This charging station is conveniently located and has plenty of charging ports. The cost is reasonable and the overall experience was great.",
#     #     "This charging station is always crowded and the charging ports are often unavailable. The cost is high and the overall experience was not good.",
#     #     "This charging station is very clean and well-maintained. The charging ports are always available and the location is great. The cost is a bit high, but worth it for the overall experience.",
#     #     "This charging station is in a bad location and the charging ports are old and unreliable. The cost is high and the overall experience was terrible.",
#     #     "This charging station is amazing! It's always clean and the charging ports are top-notch. The location is convenient and the cost is reasonable. Overall, a great experience.",
#     #     "This charging station was broken and wouldn't charge my car at all. Waste of my time and money.",
#     #     "The charging speed was incredibly slow and it took forever to get even a partial charge.",
#     #     "The station was located in a really inconvenient place with no nearby amenities or places to wait while charging.",
#     #     "The payment system was confusing and I ended up paying more than I expected.",
#     #     "The station was overcrowded and I had to wait a long time to access a charger.",
#     #     "The station was dirty and unkempt, which made me question whether it was well-maintained.",
#     #     "The charger didn't work with my particular model of EV, even though it was advertised as being compatible.",
#     #     "The price per kilowatt-hour was too high compared to other charging stations in the area.",
#     #     "There was no signage or clear instructions on how to use the charging station, which made the process frustrating and confusing.",
#     #     "The station was poorly lit and didn't feel safe to use, especially at night."

#     # ]
   


def review_pred(reviews):
    sia = SentimentIntensityAnalyzer()
    stop_words = set(stopwords.words('english'))
    sentiments = []

    for review in reviews:
        # Tokenize words and remove stop words
        words = [word.lower() for word in word_tokenize(review) if word.lower() not in stop_words]
        
        # Extract sentiment score
        sentiment = sia.polarity_scores(review)['compound']
        
        # Add sentiment score to list
        sentiments.append(sentiment)

    # Calculate overall sentiment score and map to 5-star rating
    overall_sentiment = sum(sentiments) / len(sentiments)
    rating = round((overall_sentiment + 1) * 2.5, 1)

    # Return rating
    print(rating)
    return rating
