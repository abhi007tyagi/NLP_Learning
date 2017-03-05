from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

words = ["Playing", "Cricket", "Cooked", "Game"]

for w in words:
    print(ps.stem(w))
