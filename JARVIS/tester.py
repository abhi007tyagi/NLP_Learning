import jarvis as j
import nltk
import math_expression_calculator as math_cal
import inflect
import text2num

# print(j.get_context("hello"))
# print(j.get_context("hi"))
# print(j.get_context("hey! can you move up the ladder?"))
# print(j.get_context("hey, how are you today?"))
# print(j.get_context("how's today's weather"))
# print(j.get_context("hey, add three to 4"))
# print(j.get_context("what is three multiplied to 4"))
# print(math_cal.get_math_evaluation("can you answer what 1898 subtracted from 100 is?"))
# print(math_cal.get_math_evaluation("what is the value for 10 divided by 2?"))
# print(math_cal.get_math_evaluation("multiply 7 with 5"))
# print(math_cal.get_math_evaluation("multiply 10 by 3"))
# print(math_cal.get_math_evaluation("add 5 to 2"))
# print(math_cal.get_math_evaluation("subtract 2 from 9"))
# print(math_cal.get_math_evaluation("what is 5 minus 3"))
# print(math_cal.get_math_evaluation("divide 14 by 2"))
# print(math_cal.get_math_evaluation("answer to 10 / 5"))
print(math_cal.get_math_evaluation("what is the result for 7 multiplied by 6"))
# print(math_cal.get_math_evaluation("add two thousand three hundred seventy six to 100"))
# print(math_cal.get_math_evaluation("what is three hundred seventy five multiplied by 100"))
# print(math_cal.get_math_evaluation("eleven million seventy five multiplied by 100"))
print(math_cal.get_math_evaluation("multiply 1 to 2 minus 6 plus 10 multiplied by 2 divided by 4"))
print(math_cal.get_math_evaluation("what is 10 multiplied by 6 plus 2 minus 6 plus 10 multiplied by 2 divided by 4"))
print(math_cal.get_math_evaluation("calculate forty two thousand one hundred seventy five divided by 100"))
print(math_cal.get_math_evaluation("calculate 10 / 2 - 6 + 7"))
# text = "multiply 1 to 2 minus 6 plus 10 multiplied by 2 divided by 4"
# text = "1/2+3-4="
# exp = "1*2-6+10*2/4"
# p = inflect.engine()
# print(p.number_to_words(99))
#
# print(text2num.text2num("two thousand three hundred seventy six "))
#
# tokenized = nltk.word_tokenize(text)
# tags = nltk.pos_tag(tokenized)
# print(tags)
# print(str(eval(exp)))