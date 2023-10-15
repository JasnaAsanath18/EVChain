import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer


def review_pred(reviews):
    print("REE : ",reviews)
# Example user reviews of charging stations


# Extract sentiment scores from reviews
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

    # Print rating
    print(rating)
    return rating
    # print(f"Overall rating: {rating}/5")





















