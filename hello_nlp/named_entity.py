import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

training_text = state_union.raw("2005-GWBush.txt")
input_text = state_union.raw("2006-GWBush.txt")

cust_tokenizer = PunktSentenceTokenizer(training_text)

tokenized = cust_tokenizer.tokenize(input_text)


def do_named_entity():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tags = nltk.pos_tag(words)

            named_entity = nltk.ne_chunk(tags, binary=True)

            # print(named_entity)
            named_entity.draw()
    except Exception as e:
        print(str(e))


do_named_entity()
