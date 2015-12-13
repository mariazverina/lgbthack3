import json
import nltk
import pprint
from nltk.corpus import stopwords
import string
from nltk.classify import apply_features

stop = stopwords.words('english')
stop = set(stop + "hotel room stay staff".split())

f=open('/Users/emz/Downloads/review.txt', "r")

pp = pprint.PrettyPrinter(indent=4)

all_words = []
dataset = {}

i = 0

for line in f:
    if i % 10000 == 0:
        print i
    i += 1
    j = json.loads(line)
    # pp.pprint(j)
    # offering_id = j['offering_id']
    score = j['ratings']['overall']
    review =  j['title'] + " " + j['text']
    # print score, review
    review = review.encode('ascii','ignore').lower()
    # text = [nltk.word_tokenize(s) for s in nltk.sent_tokenize(nltk.text)]
    # print nltk.word_tokenize(review)
    all_words += [w for w in nltk.word_tokenize(review) if w not in stop and w not in string.punctuation]
    dataset[review] = 'pos' if score > 3.5 else 'neg'
    # print nlp(review)

print len(all_words)


print len(dataset)
all_words = nltk.FreqDist(all_words)
word_features = list(all_words)[:2000]
print all_words.most_common(200)
print len(all_words)

def document_features(document):
    document_words = set(document.split())
    features = {}
    for word in word_features:
        features[word] = (word in document_words)
    return features

featuresets = []
for (review, clset) in dataset.items():
    x =(document_features(review), clset)
    featuresets.append(x)


tenpercent = len(dataset) / 10
print tenpercent
train_set, test_set = featuresets[tenpercent:], featuresets[:tenpercent]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(20)


