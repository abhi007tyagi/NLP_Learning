from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "I am Abhinav Tyagi. I am an Engineer and currently, I am learning NLP. This example is for detecting and " \
       "removing stop words from a sentence. "
stop_words = set(stopwords.words("english"))

words = word_tokenize(text)

filtered_text = [w for w in words if not w in stop_words]

print(filtered_text)
