import gensim.models.word2vec as word2vec
from glob import glob
from nltk.tokenize import PunktSentenceTokenizer
import re
import multiprocessing
import os

dataset_dir = "datasets"

trained_model = os.path.join(dataset_dir, "trained/word2vec.w2v")
def build_sentences():
    filenames = os.path.join(dataset_dir, "data/*.txt")
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
    sentences = build_sentences()
    model = word2vec.Word2Vec(
            sentences=sentences,
            min_count=3,
            workers=multiprocessing.cpu_count())
    model.train(sentences=sentences)
    if not os.path.exists(os.path.join(dataset_dir, "trained")):
        os.mkdir(os.path.join(dataset_dir, "trained"))
    model.save(trained_model)

# as this is to that so is this to ______
def most_similar(word1, word2, word3):
    model = word2vec.Word2Vec.load(trained_model)
    return model.most_similar(positive=[word1, word2], negative=[word3], topn=1)

# returns the most similar word to the given one
def similar_by_word(word):
    model = word2vec.Word2Vec.load(trained_model)
    return model.similar_by_word(word, topn=1)

# returns the odd one out
def doesnt_match(phrase):
    model = word2vec.Word2Vec.load(trained_model)
    return model.doesnt_match(phrase.split())


if __name__ == "__main__":
    train()
