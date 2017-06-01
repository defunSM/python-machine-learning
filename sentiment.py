import os

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from KaggleWord2VecUtility import KaggleWord2VecUtility

import pandas as pd

if __name__ == "__main__":
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data',
                                     'labeledTrainData.tsv'), header=0, delimiter="\t", quoting=3)
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'testData.tsv'), header=0, delimiter="\t", quoting=3)

    print("The first review is:")
    print(train["review"][0])
    raw_input("Press Enter to continue...")


    print("Download text data sets.")
    ntlk.download()
    clean_train_reviews = []
    print("Cleaning and parsing the training set movie reviews...\n")

    for i in range(0, len(train["review"])):
        clean_train_reviews.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(train["review"][i], true)))
