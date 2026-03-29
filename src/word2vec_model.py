from gensim.models import Word2Vec

def train_word2vec(tokenized_sentences):
    """
    tokenized_sentences = [["hello", "world"], ["what", "is", "fee"], ...]
    """

    model = Word2Vec(
        sentences=tokenized_sentences,
        vector_size=100,
        window=5,
        min_count=1,
        workers=4
    )

    return model