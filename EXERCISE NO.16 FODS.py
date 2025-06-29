import pandas as pd
from collections import Counter
import re
df = pd.read_csv("customer_reviews.csv")  
all_reviews = " ".join(df['review'].astype(str))
cleaned_text = re.sub(r'[^a-zA-Z\s]', '', all_reviews).lower()
words = cleaned_text.split()
word_freq = Counter(words)
print("Top 20 most frequent words:\n")
for word, freq in word_freq.most_common(20):
    print(f"{word}: {freq}")
