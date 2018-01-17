import json
import pandas as pd
import math
from collections import Counter
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions
from numpy import dot
from numpy.linalg import norm

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='ff57ed6a-a245-40bf-b6a0-a709612b9a7e',
    password='FOEh24Cuwubq')

csv_file = 'Papers.csv'

articles = pd.read_csv(csv_file)
articles = articles.loc[:,['Title', 'PaperText']]

doc_vectors = []
titles = []
size = len(articles.index)

for index, row in articles.iterrows():
    doc_vector = []
    title = row['Title']
    titles.append(title)
    text = row['PaperText']
    if index % 10 == 0:
        print('Extracting keywords for document ' + str(index) + ' out of ' + str(size))
    try:
        keywords = natural_language_understanding.analyze(text=text, features=Features(keywords=KeywordsOptions()))['keywords']
    except Exception as e:
        print(e.message)
        pass
    for keyword in keywords:
        doc_vector.append(keyword['text'])
    doc_vectors.append(doc_vector)

word_vector = pd.Series(doc_vectors)
articles['word_vector'] = word_vector.values

print(articles.loc[:, 'word_vector']).head()

with open('new_project.txt', 'r') as f:
    text_to_compare = f.read().replace('\n', '')

keywords_to_compare = [i['text'] for i in natural_language_understanding.analyze(text=text_to_compare, features=Features(keywords=KeywordsOptions()))['keywords']]

print(keywords_to_compare)

def compare_word_vectors(word_vec_01, word_vec_02):
    similarity = float(dot(word_vec_01,word_vec_02) / (norm(word_vec_01) * norm(word_vec_02)))
    return similarity

def naive_similarity(word_vector01, word_vector02):
    n = len(word_vector01)
    counter = 0
    matches = []
    for word in word_vector01:
        if word in word_vector02:
            counter += 1
            matches.append(word)
    print(str(counter)+ ' matches')
    return counter

def get_cosine(vec1, vec2):
     intersection = set(vec1) & set(vec2)
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([x**2 for x in vec1])
     sum2 = sum([x**2 for x in vec2])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

similarities = []

for index, row in articles.iterrows():
    if index % 10 == 0:
        print('Calculating simliarity with document number ' + str(index))
    temp_similarity = naive_similarity(keywords_to_compare, row['word_vector'])
    similarities.append(temp_similarity)

max_similarity = similarities.index(max(similarities))

print('Article with the highest similarity is ', articles.ix[index, 'Title'])
print('Matching keywords', similarities[max_similarity])
print('Keywords for that article are', articles.ix[max_similarity, 'word_vector'])

