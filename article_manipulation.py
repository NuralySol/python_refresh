import re
from collections import Counter

# Count the number of words in the article and other file manipulations
with open("./data/article.txt", "r", encoding="utf-8") as article:
    content = article.read()
    print(content)
    print("-" * 100)
    
    # Normalize the content: lowercase and remove punctuation
    cleaned_content = re.sub(r'[^\w\s]', '', content.lower())
    
    # Split the cleaned content into words
    words = cleaned_content.split()
    print(f"The number of words in the article is: {len(words)}")
    
    # Use Counter to count occurrences of each word
    word_counts = Counter(words)
    
    print("-" * 100)
    # Get the 10 most common words
    ten_common_words = dict(word_counts.most_common(10))
    print(ten_common_words)
    print("-" * 100)

# Practice: Sort the dictionary by value instead of a key and print the result
# Sort dictionary with lambda function instead of a defined function to sort by value

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(sorted_d)