import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("=" * 50)
print("  CodeAlpha - Task 3: Data Visualization")
print("=" * 50)

df = pd.read_csv('Task1_WebScraping/books_data.csv')
print(f"\n✅ Data loaded! Total books: {len(df)}")


plt.figure(figsize=(8, 5))
rating_counts = df['Rating (out of 5)'].value_counts().sort_index()
bars = plt.bar(rating_counts.index, rating_counts.values,
               color=['#FF6B6B', '#FFA07A', '#FFD700', '#90EE90', '#4CAF50'])
plt.title('Rating Distribution Of Books', fontsize=16, fontweight='bold')
plt.xlabel('Rating (Stars)', fontsize=12)
plt.ylabel('Number Of Books', fontsize=12)
plt.xticks([1, 2, 3, 4, 5], ['1 ⭐', '2 ⭐', '3 ⭐', '4 ⭐', '5 ⭐'])
for bar, count in zip(bars, rating_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
             str(count), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('chart1_rating_distribution.png', dpi=150)
plt.show()
print("✅ Chart 1 saved: chart1_rating_distribution.png")

plt.figure(figsize=(8, 5))
plt.hist(df['Price (£)'], bins=20, color='#4A90D9', edgecolor='white', linewidth=0.8)
plt.title('Price Distribution Of Books', fontsize=16, fontweight='bold')
plt.xlabel('Price (£)', fontsize=12)
plt.ylabel('Number Of Books', fontsize=12)
plt.axvline(df['Price (£)'].mean(), color='red', linestyle='--',
            linewidth=2, label=f"Average: £{df['Price (£)'].mean():.2f}")
plt.legend()
plt.tight_layout()
plt.savefig('chart2_price_distribution.png', dpi=150)
plt.show()
print("✅ Chart 2 saved: chart2_price_distribution.png")

plt.figure(figsize=(7, 7))
rating_counts = df['Rating (out of 5)'].value_counts().sort_index()
colors = ['#FF6B6B', '#FFA07A', '#FFD700', '#90EE90', '#4CAF50']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
plt.pie(rating_counts.values, labels=[f'{i} Star' for i in rating_counts.index],
        colors=colors, explode=explode, autopct='%1.1f%%',
        startangle=90, textprops={'fontsize': 11})
plt.title('Percentage Of Rating', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('chart3_rating_percentage.png', dpi=150)
plt.show()
print("✅ Chart 3 saved: chart3_rating_percentage.png")

plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x='Rating (out of 5)', y='Price (£)',
            palette=['#FF6B6B', '#FFA07A', '#FFD700', '#90EE90', '#4CAF50'])
plt.title('Price Distribution According To Rating', fontsize=16, fontweight='bold')
plt.xlabel('Rating (Stars)', fontsize=12)
plt.ylabel('Price (£)', fontsize=12)
plt.tight_layout()
plt.savefig('chart4_price_vs_rating.png', dpi=150)
plt.show()
print("✅ Chart 4 saved: chart4_price_vs_rating.png")

plt.figure(figsize=(8, 5))
avg_price = df.groupby('Rating (out of 5)')['Price (£)'].mean()
bars = plt.bar(avg_price.index, avg_price.values,
               color=['#FF6B6B', '#FFA07A', '#FFD700', '#90EE90', '#4CAF50'])
plt.title('Average Price Of Every rating', fontsize=16, fontweight='bold')
plt.xlabel('Rating (Stars)', fontsize=12)
plt.ylabel('Average Price (£)', fontsize=12)
plt.xticks([1, 2, 3, 4, 5], ['1 ⭐', '2 ⭐', '3 ⭐', '4 ⭐', '5 ⭐'])
for bar, price in zip(bars, avg_price.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             f'£{price:.1f}', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('chart5_avg_price_per_rating.png', dpi=150)
plt.show()
print("✅ Chart 5 saved: chart5_avg_price_per_rating.png")

print("\n" + "=" * 50)
print("  🎉 ALL 5 CHARTS HAVE BEEN CREATED!")
print("  Charts have been saved in the folder!!")
print("=" * 50)