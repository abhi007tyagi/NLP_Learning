from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("change", pos="v"))
print(lemmatizer.lemmatize("better", pos="a"))
