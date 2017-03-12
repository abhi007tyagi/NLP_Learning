import nltk

text1 = "can you answer what 10 / 2 is?"
text2 = "can you answer what 10 divided by 2 is?"

tokenized1 = nltk.word_tokenize(text1);
tags1 = nltk.pos_tag(tokenized1)
print(tags1)

tokenized2 = nltk.word_tokenize(text2);
tags2 = nltk.pos_tag(tokenized2)
print(tags2)

chunkPattern = r"""Chunk: {<CD>*<JJ|VBN><IN>*<CD>}"""
chunkParser = nltk.RegexpParser(chunkPattern)
chunkedData = chunkParser.parse(tags1)
print("FIRST-->", chunkedData)

chunkedData = chunkParser.parse(tags2)
print("SECOND-->", chunkedData)
