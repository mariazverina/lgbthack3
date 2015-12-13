import pickle
import json

f=open('/Users/emz/Downloads/review.txt', "r")

all_reviews = []
for line in f:
    j = json.loads(line)
    # pp.pprint(j)
    offering_id = j['offering_id']
    score = j['ratings']['overall']
    review =  j['title'] + " " + j['text']

    review = review.encode('ascii','ignore').lower()
    all_reviews.append((offering_id, score, review))


fw = open('/Users/emz/Downloads/review.p', "w")
pickle.dump(all_reviews, fw)
