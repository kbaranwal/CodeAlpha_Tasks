import requests
from bs4 import BeautifulSoup
import pandas as pd

books_data = []

print("🚀 Scraping shuru ho rahi hai...")

for page in range(1, 51):
    
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        
        title = book.find('h3').find('a')['title']
        
        price = book.find('p', class_='price_color').text.strip()
        price = price.replace('£', '').replace('Â', '').strip()
        
        rating_word = book.find('p', class_='star-rating')['class'][1]
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        rating = rating_map.get(rating_word, 0)
        
        availability = book.find('p', class_='instock availability').text.strip()
        
        books_data.append({
            'Title': title,
            'Price (£)': float(price),
            'Rating (out of 5)': rating,
            'Availability': availability
        })
    
    print(f"✅ Page {page}/50 done — {len(books_data)} books collected so far")

df = pd.DataFrame(books_data)

df.to_csv('books_data.csv', index=False)

print("\n🎉 Scraping complete!")
print(f"📊 Total books scraped: {len(df)}")
print(f"💾 File saved: books_data.csv")
print("\n📈 Quick Summary:")
print(f"   Average Price: £{df['Price (£)'].mean():.2f}")
print(f"   Most Common Rating: {df['Rating (out of 5)'].mode()[0]} stars")
print(f"   Cheapest Book: £{df['Price (£)'].min()}")
print(f"   Most Expensive Book: £{df['Price (£)'].max()}")
