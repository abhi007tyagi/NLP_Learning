import nltk


def get_exp(chunked):
    exp = ""
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
        for l in subtree.leaves():
            exp += " " + str(l[0])

    print("get_exp ->", exp)
    return exp


def check_word_action(exp):
    if "multiplied by" in exp:
        exp = exp.replace("multiplied by", "*")
        return exp
    if "x" in exp:
        exp = exp.replace("x", "*")
        return exp
    if "divided by" in exp:
        exp = exp.replace("divided by", "/")
        return exp
    if "plus" in exp:
        exp = exp.replace("plus", "+")
        return exp
    if "minus" in exp:
        exp = exp.replace("minus", "-")
        return exp
    if "subtracted from" in exp:
        exp = exp.replace("subtracted from", "-")
        return exp[::-1]
    return exp


text1 = "can you answer what 10 x 2 is?"
text2 = "what is the value for 10 divided by 2?"

tokenized1 = nltk.word_tokenize(text1);
tags1 = nltk.pos_tag(tokenized1)
# print(tags1)

tokenized2 = nltk.word_tokenize(text2);
tags2 = nltk.pos_tag(tokenized2)
# print(tags2)

chunkPattern = r"""Chunk: {<CD>*<JJ|VBN><IN>*<CD>}"""
chunkParser = nltk.RegexpParser(chunkPattern)
chunkedData = chunkParser.parse(tags1)
# print("FIRST-->", chunkedData)

expression = check_word_action(get_exp(chunkedData))
print(expression)
print(eval(expression))

chunkedData = chunkParser.parse(tags2)
# print("SECOND-->", chunkedData)

expression = check_word_action(get_exp(chunkedData))
print(expression)
print(eval(expression))
