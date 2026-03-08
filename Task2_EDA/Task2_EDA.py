import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("  CodeAlpha - Task 2: Exploratory Data Analysis")
print("=" * 50)

# ----------------------------------------
# Step 1: Data Load karo
# ----------------------------------------
df = pd.read_csv('Task1_WebScraping/books_data.csv')

print("\n📂 DATA LOAD HO GAYI!")
print(f"   Total Books: {len(df)}")
print(f"   Total Columns: {len(df.columns)}")

# ----------------------------------------
# Step 2: Data ka Structure dekho
# ----------------------------------------
print("\n📋 COLUMNS:")
print(df.columns.tolist())

print("\n📊 PEHLI 5 BOOKS:")
print(df.head())

print("\n🔍 DATA TYPES:")
print(df.dtypes)

# ----------------------------------------
# Step 3: Missing Data check karo
# ----------------------------------------
print("\n❓ MISSING VALUES:")
print(df.isnull().sum())
print("✅ Koi missing value nahi hai!" if df.isnull().sum().sum() == 0 else "⚠️ Missing values hain!")

# ----------------------------------------
# Step 4: Basic Statistics
# ----------------------------------------
print("\n📈 BASIC STATISTICS:")
print(df.describe())

# ----------------------------------------
# Step 5: Price Analysis
# ----------------------------------------
print("\n💰 PRICE ANALYSIS:")
print(f"   Sabse Sasti Book:    £{df['Price (£)'].min()}")
print(f"   Sabse Mehngi Book:   £{df['Price (£)'].max()}")
print(f"   Average Price:       £{df['Price (£)'].mean():.2f}")
print(f"   Median Price:        £{df['Price (£)'].median():.2f}")

# Sabse sasti book
cheapest = df[df['Price (£)'] == df['Price (£)'].min()]['Title'].values[0]
print(f"   Sabse Sasti Book:    {cheapest}")

# Sabse mehngi book
expensive = df[df['Price (£)'] == df['Price (£)'].max()]['Title'].values[0]
print(f"   Sabse Mehngi Book:   {expensive}")

# ----------------------------------------
# Step 6: Rating Analysis
# ----------------------------------------
print("\n⭐ RATING ANALYSIS:")
rating_counts = df['Rating (out of 5)'].value_counts().sort_index()
for rating, count in rating_counts.items():
    bar = "⭐" * rating
    print(f"   {bar} ({rating} stars): {count} books")

most_common_rating = df['Rating (out of 5)'].mode()[0]
print(f"\n   Sabse Common Rating: {most_common_rating} stars")

# ----------------------------------------
# Step 7: Rating ke hisaab se Average Price
# ----------------------------------------
print("\n💡 RATING KE HISAAB SE AVERAGE PRICE:")
avg_price_by_rating = df.groupby('Rating (out of 5)')['Price (£)'].mean().round(2)
for rating, price in avg_price_by_rating.items():
    print(f"   {rating} stars → Average Price: £{price}")

# ----------------------------------------
# Step 8: Price Range Analysis
# ----------------------------------------
print("\n📦 PRICE RANGE ANALYSIS:")
df['Price Range'] = pd.cut(df['Price (£)'],
                           bins=[0, 20, 40, 60],
                           labels=['Sasta (£0-20)', 'Medium (£20-40)', 'Mehngi (£40-60)'])
price_range_counts = df['Price Range'].value_counts()
for range_name, count in price_range_counts.items():
    print(f"   {range_name}: {count} books")

# ----------------------------------------
# Step 9: Availability Check
# ----------------------------------------
print("\n✅ AVAILABILITY:")
print(df['Availability'].value_counts())

print("\n" + "=" * 50)
print("  ✅ EDA COMPLETE!")
print("=" * 50)