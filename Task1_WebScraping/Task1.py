# ============================================
# CodeAlpha Internship - Task 1: Web Scraping
# Website: books.toscrape.com
# ============================================

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Yahan saara data store hoga
books_data = []

print("🚀 Scraping shuru ho rahi hai...")

# Website ke 50 pages hain, sab scrape karenge
for page in range(1, 51):
    
    # Har page ka URL banao
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    
    # Website se HTML download karo
    response = requests.get(url)
    
    # HTML ko parse karo
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Is page ki saari books dhundo
    books = soup.find_all('article', class_='product_pod')
    
    # Har book ka data nikalo
    for book in books:
        
        # Book ka naam
        title = book.find('h3').find('a')['title']
        
        # Book ki price (£ sign hatao)
        price = book.find('p', class_='price_color').text.strip()
        price = price.replace('£', '').replace('Â', '').strip()
        
        # Book ki rating (word to number convert)
        rating_word = book.find('p', class_='star-rating')['class'][1]
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        rating = rating_map.get(rating_word, 0)
        
        # Book available hai ya nahi
        availability = book.find('p', class_='instock availability').text.strip()
        
        # Data list mein add karo
        books_data.append({
            'Title': title,
            'Price (£)': float(price),
            'Rating (out of 5)': rating,
            'Availability': availability
        })
    
    print(f"✅ Page {page}/50 done — {len(books_data)} books collected so far")

# Pandas DataFrame banao
df = pd.DataFrame(books_data)

# CSV file mein save karo
df.to_csv('books_data.csv', index=False)

print("\n🎉 Scraping complete!")
print(f"📊 Total books scraped: {len(df)}")
print(f"💾 File saved: books_data.csv")
print("\n📈 Quick Summary:")
print(f"   Average Price: £{df['Price (£)'].mean():.2f}")
print(f"   Most Common Rating: {df['Rating (out of 5)'].mode()[0]} stars")
print(f"   Cheapest Book: £{df['Price (£)'].min()}")
print(f"   Most Expensive Book: £{df['Price (£)'].max()}")
