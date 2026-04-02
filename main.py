#partie word2vec

'''from src.data_loader import load_dataset, extract_pairs
from src.preprocessing import clean_text, normalize_text, tokenize_text, extract_tokens_only
from src.word2vec_model import train_word2vec

def main():
    path = "data/raw/chatbot.json"

    data = load_dataset(path)
    pairs = extract_pairs(data)

    print("Nombre de paires :", len(pairs))

    all_sentences = []

    for pair in pairs:
        text = pair["input"]

        text = clean_text(text)
        text = normalize_text(text)
        tokenized = tokenize_text(text)

        tokens = extract_tokens_only(tokenized)
        all_sentences.extend(tokens)

    print("Exemple tokens :", all_sentences[:3])

    # Avec word2vec
    model = train_word2vec(all_sentences)

    # Test.py après deplacement à main.py
    print ("Vecteur de 'hello':")
    print(model.wv["hello"])
    print ("\nMots similaires a 'hello':")
    print(model.wv.most_similar("hello"))
    print (model.wv.most_similar("fee"))


if __name__ == "__main__":
    main()'''


#partie BERT
from src.bert_vectorizer import get_bert_embedding

def main():
    sentence = "What is the fee?"

    embedding = get_bert_embedding(sentence)

    print("Taille du vecteur :", len(embedding))
    print("Début du vecteur :", embedding[:10])

    #print(get_bert_embedding("Hello"))
    #print(get_bert_embedding("Hi"))
    #print(get_bert_embedding("Heyy"))
    
if __name__ == "__main__":
    main()