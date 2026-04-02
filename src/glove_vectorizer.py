import gensim.downloader as api
import numpy as np
import ssl


ssl._create_default_https_context = ssl._create_unverified_context # WARNING: temporary fix for SSL issue (not secure)

def load_glove_model():
    print("Chargement du modèle GloVe...")
    model = api.load("glove-wiki-gigaword-100")#entrainé sur wikipedia et gigaword
    print("Modèle chargé !")
    return model

def sentence_to_vector(sentence_tokens, model):
    vectors = []

    for word in sentence_tokens:
        if word in model:
            vectors.append(model[word])

    if len(vectors) == 0:
        return np.zeros(100)

    return np.mean(vectors, axis=0)