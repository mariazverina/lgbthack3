import pickle
import re
from collections import Counter

fr = open('/Users/emz/Downloads/review.p', "r")

mw = pickle.load(fr)
print len(mw)

gay_props = []
for (offering_id, score, review) in mw:
    if re.match('gay ', review):
        gay_props.append(offering_id)


print Counter(gay_props).most_common(20)
