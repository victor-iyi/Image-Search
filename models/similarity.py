import gensim.models.word2vec as word2vec
from glob import glob
from nltk.tokenize import PunktSentenceTokenizer
import re
import multiprocessing
import os

from helpers.config import DATASET_PATH

trained_model = os.path.join(DATASET_PATH, "trained/word2vec.w2v")


def build_sentences():
    """
    Builds list of sentences.
    :return: List of sentences -> (list of words)
    """
    filenames = os.path.join(DATASET_PATH, "data/*.txt")
    filenames = glob(filenames)
    corpus = ""
    for filename in filenames:
        with open(filename) as f:
            corpus += f.read()
            print("Corpus is now {:,} characters long".format(len(corpus)))

    tokenizer = PunktSentenceTokenizer()
    raw_sentences = tokenizer.tokenize(corpus)

    def word_list(raw):
        clean_words = re.sub(r"[^a-zA-Z]", " ", raw)
        return clean_words.split()

    sentences = []
    for raw_sentence in raw_sentences:
        sentences.append(word_list(raw_sentence))
    return sentences


def train():
    """
    Train the word2Vec model
    """
    sentences = build_sentences()
    model = word2vec.Word2Vec(
        sentences=sentences,
        min_count=3,
        workers=multiprocessing.cpu_count())
    model.build_vocab(sentences)
    model.train(sentences=sentences)
    if not os.path.exists(os.path.join(DATASET_PATH, "trained")):
        os.mkdir(os.path.join(DATASET_PATH, "trained"))
    model.save(trained_model)


# as this is to that so is this to ______
def most_similar(word1, word2, word3):
    """
    As {word1} is to {word2}. So is {word3} to ______.
    :param word1: Word compared to word2.
    :param word2: Word compared to word1.
    :param word3: Word compared to result based on word1 & word2.
    :return: returns most similar match to word3
    based on the similarity score of word1 & word2.
    """
    model = word2vec.Word2Vec.load(trained_model)
    return model.most_similar(positive=[word1, word2], negative=[word3], topn=1)


def similar_by_word(word):
    """
    Returns the most similar word to a given word.
    :param word: Word to find it's most similar word.
    :return: most similar word to given word.
    """
    model = word2vec.Word2Vec.load(trained_model)
    return model.similar_by_word(word, topn=1)


def doesnt_match(phrase):
    """
    Fetches the odd word out in a given phrase
    :param phrase: Phrase containing odd word.
    :return: Odd word in phrase.
    """
    model = word2vec.Word2Vec.load(trained_model)
    return model.doesnt_match(phrase.split())


if __name__ == "__main__":
    train()
