#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from bs4 import BeautifulSoup
import os


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS

from nltk.stem import SnowballStemmer
import pymorphy2
import stopwords
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn


BASE_DIR = '../data/base/'
TEST_DIR = '../data/test/'


class LemmaTokenizer(object):
    def __init__(self):
        # self.wnl = WordNetLemmatizer()
        self.wnl = SnowballStemmer('english')
        self.morph = pymorphy2.MorphAnalyzer()

    def __call__(self, text):
        tokenz = CountVectorizer().build_tokenizer()(text)
        lemmas = []
        for t in tokenz:
            if len(t) > 2:
                p = self.morph.parse(t)
                if 'LATN' in p[0].tag:  # and re.search('!\d+', p[0].normal_form)
                    # lemmas.append(self.wnl.lemmatize(t))
                    lemmas.append(self.wnl.stem(t))
                elif 'NUMB' in p[0].tag:
                    continue
                elif 'UNKN' in p[0].tag:
                    continue
                elif 'ROMN' in p[0].tag:
                    continue
                else:
                    lemmas.append(p[0].normal_form)
        return lemmas


def main():
    df_train = pd.DataFrame(columns=['fname', 'txt'])
    for filename in os.listdir(BASE_DIR):
        with open(os.path.join(BASE_DIR, filename), 'r') as bf:
            txt = BeautifulSoup(bf.read(), 'lxml').get_text()
            df_train.loc[len(df_train)] = [filename, txt]

    df_test = pd.DataFrame(columns=['fname', 'txt'])
    for filename in os.listdir(TEST_DIR):
        with open(os.path.join(TEST_DIR, filename), 'r') as bf:
            txt = BeautifulSoup(bf.read(), 'lxml').get_text()
            df_test.loc[len(df_test)] = [filename, txt]

    # print df_train
    # print df_test
    df_all = pd.concat([df_train, df_test], ignore_index=True)
    # print df_all

    stop_words = stopwords.get_stopwords('english') + stopwords.get_stopwords('russian')
    # tfidf_vec = TfidfVectorizer(tokenizer=LemmaTokenizer(), stop_words=stop_words)
    dtm_vec = CountVectorizer(tokenizer=LemmaTokenizer(), stop_words=stop_words)
    dtm = dtm_vec.fit_transform(df_all['txt'].values.tolist()).toarray()

    dist = 1 - cosine_similarity(dtm)
    # pairwise_similarity = tfidf * tfidf.T

    print dist
    # print pairwise_similarity
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    pos = mds.fit_transform(dist)

    xs, ys = pos[:, 0], pos[:, 1]
    names = df_all['fname'].values.tolist()
    for x, y, name in zip(xs, ys, names):
        # color = 'orange' if "Austen" in name else 'skyblue'
        plt.scatter(x, y)
        plt.text(x, y, name)
    plt.show()


if __name__ == "__main__":
    main()
