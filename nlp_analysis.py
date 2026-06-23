import pandas as pd
from textblob import TextBlob

# Sample reviews dataset
reviews = [
    "The product is excellent and easy to use.",
    "I am very happy with the service.",
    "The experience was average.",
    "The product quality is poor.",
    "I am disappointed with the delivery."
]

df = pd.DataFrame({"Review": reviews})

# Sentiment Analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(get_sentiment)

print(df)

# Save results
df.to_csv("sentiment_results.csv", index=False)

print("\nSentiment analysis completed successfully!")