import csv
import re

KEYWORDS_DICT = {}
# load relevance file
with open('relevance_scores.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        KEYWORDS_DICT[row[0]] = int(row[1])

class Article:
    def __init__(self, href, title, authors):
        self.href = href
        self.title = title
        self.authors = authors
        self.score = self.get_relevance_score()

    def get_relevance_score(self):
        score = 0
        for key in KEYWORDS_DICT.keys():
            if re.search(key, self.title, re.IGNORECASE):
                score += KEYWORDS_DICT[key]
        return score