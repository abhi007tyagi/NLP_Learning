import nltk
import text2num as t2n
import re
from nltk.corpus import stopwords


def get_exp(chunked):
    exp = extract_chunks(chunked, ["Chunk00", "Chunk1", "Chunk2", "Chunk3"])
    # print("get_exp ->", exp)
    return exp


def extract_chunks(chunked, tags):
    exp = ""
    digit = ""
    for subtree in chunked.subtrees(filter=lambda t: t.label() in tags):
        for l in subtree.leaves():
            print("l[0] -->>> ", str(l[0]))
            if str(l[0]) not in ["+", "-", "*", "/", "x", "X", "plus", "minus", "multiplied", "divided"]:
                digit += str(l[0]) + " "
            else:
                try:
                    digit = str(t2n.text2num(digit[:-1]))
                    digit += " " + str(l[0])
                    exp += " " + digit
                    digit = ""
                except Exception as e:
                    print("text2num error ->", e.args)
    if len(digit) > 0:
        exp += " " + digit
    return exp


def extract_direct_math_expressions(tags):
    exp = ""
    stack = []
    counter = 0
    for word in tags:
        if "add" == word[0]:
            stack.append(" + ")
        elif "subtract" == word[0] or "subtracted" == word[0]:
            stack.append(" - ")
        elif "multiply" == word[0]:
            stack.append(" * ")
        elif "divide" == word[0]:
            stack.append(" / ")
        elif "plus" == word[0] or "+" == word[0] or "added" == word[0]:
            exp += " + "
        elif "minus" == word[0] or "-" == word[0]:
            exp += " - "
        elif "multiplied" == word[0] or "*" == word[0] or "x" == word[0] or "X" == word[0]:
            exp += " * "
        elif "divided" == word[0] or "/" == word[0]:
            exp += " / "

        if word[1] == "CD":
            exp += str(word[0])
        if counter > 0 and len(stack) > 0:
            exp += stack.pop()

        counter += 1

    # print(exp, " = "+str(eval(exp)))
    return str(eval(exp))


def check_word_action(exp):
    if "multiplied" in exp:
        exp = exp.replace("multiplied", "*")
        return exp
    if "multiplied" in exp:
        exp = exp.replace("multiplied", "*")
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
    if "X" in exp:
        exp = exp.replace("X", "*")
        return exp
    if "divided" in exp:
        exp = exp.replace("divided", "/")
        return exp
    if "divide" in exp:
        exp = exp.replace("divide", "")
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
    if "added" in exp:
        exp = exp.replace("added", "+")
        return exp
    if "minus" in exp:
        exp = exp.replace("minus", "-")
        return exp
    if "subtracted" in exp:
        temp = exp.split(" subtracted ")
        exp = temp[1] + " - " + temp[0]
        return exp
    if "subtract" in exp:
        exp = exp.replace("subtract", "")
        if "from" in exp:
            temp = exp.split(" from ")
            exp = temp[1] + " - " + temp[0]
            return exp
    return exp


def format_input(text):
    regex = r"[0-9][*+/xX-][0-9]"
    if re.search(regex, text):
        if "-" in text:
            text = text.replace("-", " - ")
        if "+" in text:
            text = text.replace("+", " + ")
        if "*" in text:
            text = text.replace("*", " * ")
        if "/" in text:
            text = text.replace("/", " / ")
        if "x" in text:
            text = text.replace("x", " x ")
        if "X" in text:
            text = text.replace("X", " X ")
        if "calculate" in text:
            text = text.replace("calculate", "")
    return text


def text_to_num(text):
    tokenized = nltk.word_tokenize(text);
    tags = nltk.pos_tag(tokenized)
    print(tags)
    chunkPattern = r""" Chunk0: {((<NN|CD.?|RB>)<CD.?|VBD.?|VBP.?|VBN.?|NN.?|RB.?|JJ>*)<NN|CD.?>} """
    chunkParser = nltk.RegexpParser(chunkPattern)
    chunkedData = chunkParser.parse(tags)
    print(chunkedData)

    for subtree in chunkedData.subtrees(filter=lambda t: t.label() in "Chunk0"):
        exp = ""
        for l in subtree.leaves():
            exp += str(l[0]) + " "
        exp = exp[:-1]
        print(exp)
        try:
            text = text.replace(exp, str(t2n.text2num(exp)))
        except Exception as e:
            print("error text2num ->", e.args)
        print(text)
    return text


def get_math_evaluation(text):
    # print(text)

    # formatting the input text
    text = format_input(text)
    # print(text)
    result = ""

    # convert word numbers to digits
    text = text_to_num(text)

    # calculating simple expression like 10/2+2
    try:
        # removing any spaces
        exp = text.replace(" ", "")
        # print(exp)
        result = str(eval(exp))
    except Exception as e:
        print("error 1 -> ", e.args)

    # if result length is zero it means simple calculation failed proceed to second method
    if len(result) == 0:

        # tokenize and remove stop words
        tokenized = nltk.word_tokenize(text)

        stop_words = set(stopwords.words("english"))
        filtered_text = [w for w in tokenized if not w in stop_words]
        # print(filtered_text)

        #  tag the filtered words
        tags = nltk.pos_tag(filtered_text)
        # print(tags)

        # calculating direct math expressions like "add 10 to 6 multiplied by 7 divided by 6
        try:
            result = extract_direct_math_expressions(tags)
        except Exception as e:
            print("error 2 -> ", e.args)

        # if result length is zero it means second calculation failed proceed to the third rule based approach
        if len(result) == 0:
            # do the chunking of tags
            chunk_pattern = r"""
                                Chunk00: {((<NN|CD.?|RB|VB>)<CD.?|VBD.?|VBP.?|VBN.?|NN.?|RB.?|JJ.?>*)<NN|CD.?>}
                                Chunk1: {<VB|VBP|RB|VBD|JJ|NNS><CD*><IN|TO><CD*>}
                                Chunk2: {<RB.?|CD*><JJ|VB|VBP|VBN|VBD|NNS|NN|CC><IN|TO><CD*>}
                                Chunk3: {<RB.?|CD*><JJ|VBP|VB|VBN|VBD|NNS|NN|:|CC><CD*>}
                            """
            chunk_parser = nltk.RegexpParser(chunk_pattern)
            chunked_data = chunk_parser.parse(tags)
            print(chunked_data)

            exp = get_exp(chunked_data)
            result = "Can't extract expression!"
            if len(exp) >= 2:
                try:
                    expression = check_word_action(exp)
                    result = str(eval(expression))
                except Exception as e:
                    print("error 3 ->", e.args)
                    # return str(expression + " = " + str(eval(expression)))
                    # else:
                    #     print("issue")

    return result
