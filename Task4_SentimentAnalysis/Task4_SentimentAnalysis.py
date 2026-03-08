import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

print("=" * 50)
print("  CodeAlpha - Task 4: Sentiment Analysis")
print("=" * 50)

df = pd.read_csv('Task1_WebScraping/books_data.csv')
print(f"\nData Loaded! Total books: {len(df)}")

def rating_to_sentiment(rating):
    if rating <= 2:
        return 'Negative'
    elif rating == 3:
        return 'Neutral'
    else:
        return 'Positive'

df['Sentiment'] = df['Rating (out of 5)'].apply(rating_to_sentiment)

print("\nSENTIMENT DISTRIBUTION (Rating Based):")
sentiment_counts = df['Sentiment'].value_counts()
for sentiment, count in sentiment_counts.items():
    print(f"   {sentiment}: {count} books")

print("\nAnalyzing Book Titles using VADER...")
sia = SentimentIntensityAnalyzer()

def analyze_title_sentiment(title):
    score = sia.polarity_scores(title)
    compound = score['compound']
    if compound >= 0.05:
        return 'Positive', compound
    elif compound <= -0.05:
        return 'Negative', compound
    else:
        return 'Neutral', compound

df['Title_Sentiment'], df['Compound_Score'] = zip(*df['Title'].apply(analyze_title_sentiment))

print("\nTITLE SENTIMENT DISTRIBUTION (VADER):")
title_sentiment_counts = df['Title_Sentiment'].value_counts()
for sentiment, count in title_sentiment_counts.items():
    print(f"   {sentiment}: {count} books")

print("\nTOP 5 MOST POSITIVE TITLES:")
top_positive = df.nlargest(5, 'Compound_Score')[['Title', 'Compound_Score', 'Rating (out of 5)']]
for _, row in top_positive.iterrows():
    print(f"   {row['Title'][:50]}")
    print(f"   Score: {row['Compound_Score']:.3f} | Rating: {row['Rating (out of 5)']} stars")

print("\nTOP 5 MOST NEGATIVE TITLES:")
top_negative = df.nsmallest(5, 'Compound_Score')[['Title', 'Compound_Score', 'Rating (out of 5)']]
for _, row in top_negative.iterrows():
    print(f"   {row['Title'][:50]}")
    print(f"   Score: {row['Compound_Score']:.3f} | Rating: {row['Rating (out of 5)']} stars")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('CodeAlpha - Sentiment Analysis Results', fontsize=16, fontweight='bold')

colors1 = ['#FF6B6B', '#FFD700', '#4CAF50']
sentiment_order = ['Negative', 'Neutral', 'Positive']
counts1 = [sentiment_counts.get(s, 0) for s in sentiment_order]
bars1 = axes[0].bar(sentiment_order, counts1, color=colors1, edgecolor='white')
axes[0].set_title('Rating Based Sentiment', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Sentiment', fontsize=11)
axes[0].set_ylabel('Number of Books', fontsize=11)
for bar, count in zip(bars1, counts1):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                str(count), ha='center', fontweight='bold')

colors2 = ['#4CAF50', '#FF6B6B', '#FFD700']
title_order = ['Positive', 'Negative', 'Neutral']
counts2 = [title_sentiment_counts.get(s, 0) for s in title_order]
bars2 = axes[1].bar(title_order, counts2, color=colors2, edgecolor='white')
axes[1].set_title('Title Based Sentiment (VADER)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Sentiment', fontsize=11)
axes[1].set_ylabel('Number of Books', fontsize=11)
for bar, count in zip(bars2, counts2):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                str(count), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('chart6_sentiment_analysis.png', dpi=150)
plt.show()
print("\nChart saved: chart6_sentiment_analysis.png")

print("\n" + "=" * 50)
print("  FINAL SUMMARY:")
print("=" * 50)
positive_pct = (sentiment_counts.get('Positive', 0) / len(df)) * 100
negative_pct = (sentiment_counts.get('Negative', 0) / len(df)) * 100
neutral_pct = (sentiment_counts.get('Neutral', 0) / len(df)) * 100
print(f"  Positive Books: {positive_pct:.1f}%")
print(f"  Neutral Books:  {neutral_pct:.1f}%")
print(f"  Negative Books: {negative_pct:.1f}%")
print("\n  Sentiment Analysis Complete!")
print("=" * 50)