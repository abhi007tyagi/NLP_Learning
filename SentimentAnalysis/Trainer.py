import nltk
from nltk.tokenize import word_tokenize
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

print("Reading training corpus...")

positive = open("raw/positive.txt", "r").read()
negative = open("raw/negative.txt", "r").read()

print("Building documents and words...")

all_words = []
documents = []

#  j is adject, r is adverb, and v is verb
# allowed_word_types = ["J","R","V"]
allowed_word_types = ["J"]

for p in positive.split("\n"):
    documents.append((p, "pos"))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for n in negative.split("\n"):
    documents.append((n, "neg"))
    words = word_tokenize(n)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

print("Saving documents...")

save_documents = open("pickled/documents.pickle", "wb")
pickle.dump(documents, save_documents)
save_documents.close()

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

print("Saving words...")

save_word_features = open("pickled/word_features5k.pickle", "wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


featuresets = [(find_features(rev), category) for (rev, category) in documents]
random.shuffle(featuresets)

save_featureset = open("pickled/featuresets.pickle", "wb")
pickle.dump(featuresets, save_featureset)
save_featureset.close()

print("Feature-set created of length ->", len(featuresets))

training_set = featuresets[:10000]
testing_set = featuresets[10000:]

print("Starting training different algorithms...")

orig_classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original_classifier Accuracy ->", (nltk.classify.accuracy(orig_classifier, testing_set)) * 100)

save_classifier = open("pickled/originalnaivebayes5k.pickle", "wb")
pickle.dump(orig_classifier, save_classifier)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier Accuracy ->", (nltk.classify.accuracy(MNB_classifier, testing_set)) * 100)

save_classifier = open("pickled/MNB_classifier5k.pickle", "wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier Accuracy ->", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set)) * 100)

save_classifier = open("pickled/BernoulliNB_classifier5k.pickle", "wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier Accuracy ->", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)) * 100)

save_classifier = open("pickled/LogisticRegression_classifier5k.pickle", "wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier Accuracy ->", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set)) * 100)

save_classifier = open("pickled/SGDC_classifier5k.pickle", "wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier.close()

# SVC_classifier = SklearnClassifier(SVC())
# SVC_classifier.train(training_set)
# print("SVC_classifier Accuracy ->", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier Accuracy ->", (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) * 100)

save_classifier = open("pickled/LinearSVC_classifier5k.pickle", "wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

# NuSVC_classifier = SklearnClassifier(NuSVC())
# NuSVC_classifier.train(training_set)
# print("NuSVC_classifier Accuracy ->", (nltk.classify.accuracy(NuSVC_classifier, testing_set)) * 100)

# custom_classifier = CustomClassifier(SGDClassifier, LinearSVC_classifier, LogisticRegression_classifier,
#                                      BernoulliNB_classifier, MNB_classifier)
# print("Custom_classifier Accuracy ->", (nltk.classify.accuracy(custom_classifier, testing_set)) * 100)
