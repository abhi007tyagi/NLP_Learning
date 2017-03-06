import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

training_text = state_union.raw("2005-GWBush.txt")
input_text = state_union.raw("2006-GWBush.txt")

cust_tokenizer = PunktSentenceTokenizer(training_text)

tokenized = cust_tokenizer.tokenize(input_text)


def do_chinking():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tags = nltk.pos_tag(words)
            chinkPattern = r"""Chink: {<.*>+}
                                       }<VB.?|IN|DT|TO>+{"""

            chinkParser = nltk.RegexpParser(chinkPattern)
            chinkedData = chinkParser.parse(tags)

            # print(chinkedData)
            chinkedData.draw()
    except Exception as e:
        print(str(e))


do_chinking()
