from nltk.corpus import wordnet

ss = wordnet.synsets("good")

print(ss)

print(ss[0].name())

print(ss[0].lemmas()[0].name())

print(ss[0].definition())

print(ss[0].examples())

synonyms = []
antonyms = []

for syn in ss:
    for lem in syn.lemmas():
        synonyms.append(lem.name())
        if lem.antonyms():
            antonyms.append(lem.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

word1 = wordnet.synset("adapt.v.01")
word2 = wordnet.synset("modify.v.01")

print(word1.wup_similarity(word2))
