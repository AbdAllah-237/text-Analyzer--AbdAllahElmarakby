import string
file_path = input("Enter the path to your text file: ")
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()
    

import re
from collections import Counter

def analyze_text(text):
    # Sentence count ( )
    cleaned_for_sentences = re.sub(r'(\d)\.(\d)', r'\1\2', text)
    sentence_count = len(re.findall(r'[.!:?]+', cleaned_for_sentences))

    # Text cleaning
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, " ")

    words = text.split()
    word_count = len(words)

    top_words = Counter(words).most_common(10)

    return word_count, sentence_count, top_words
if __name__ == "__main__":
    with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

    word_count, sentence_count, top_words = analyze_text(text)

    print("Word Count:", word_count)
    print("Sentence Count:", sentence_count)
    print("Top 10 Most Frequent Words:")

    for word, count in top_words:

        print(f"{word}: {count}")
