import nltk


def get_exp(chunked):

    exp = extract_chunks(chunked, "Chunk1")

    if len(exp) == 0:
        # print("second check")
        exp = extract_chunks(chunked, "Chunk2")

    # print("get_exp ->", exp)
    return exp


def extract_chunks(chunked, tag):
    exp = ""
    for subtree in chunked.subtrees(filter=lambda t: t.label() == tag):
        for l in subtree.leaves():
            exp += " " + str(l[0])
    return exp


def check_word_action(exp):
    if "multiplied by" in exp:
        exp = exp.replace("multiplied by", "*")
        return exp
    if "multiply" in exp:
        exp = exp.replace("multiply ", "")
        if "with" in exp:
            exp = exp.replace("with", "*")
            return exp
        if "by" in exp:
            exp = exp.replace("by", "*")
            return exp
    if "x" in exp:
        exp = exp.replace("x", "*")
        return exp
    if "divided by" in exp:
        exp = exp.replace("divided by", "/")
        return exp
    if "divide" in exp:
        exp = exp.replace("divide ", "")
        if "with" in exp:
            exp = exp.replace("with", "/")
            return exp
        if "by" in exp:
            exp = exp.replace("by", "/")
            return exp
    if "plus" in exp:
        exp = exp.replace("plus", "+")
        return exp
    if "add" in exp:
        exp = exp.replace("add ", "")
        if "in" in exp:
            exp = exp.replace("in", "+")
            return exp
        if "to" in exp:
            exp = exp.replace("to", "+")
            return exp
    if "added to" in exp:
        exp = exp.replace("added to", "+")
        return exp
    if "minus" in exp:
        exp = exp.replace("minus", "-")
        return exp
    if "subtracted from" in exp:
        temp = exp.split(" subtracted from ")
        exp = temp[1] + " - " + temp[0]
        return exp
    if "subtract" in exp:
        exp = exp.replace("subtract ", "")
        if "from" in exp:
            temp = exp.split(" from ")
            exp = temp[1] + " - " + temp[0]
            return exp
    return exp


def get_math_evaluation(text):
    tokenized = nltk.word_tokenize(text);
    tags = nltk.pos_tag(tokenized)
    # print(tags)

    chunkPattern = r"""Chunk1: {<RB|VBD|JJ><CD><IN|TO><CD>}
                       Chunk2: {<CD><JJ|VBN|VBD><IN|TO><CD>} """
    chunkParser = nltk.RegexpParser(chunkPattern)
    chunkedData = chunkParser.parse(tags)
    # print(chunkedData)

    expression = check_word_action(get_exp(chunkedData))
    print(expression + " = ", eval(expression))
