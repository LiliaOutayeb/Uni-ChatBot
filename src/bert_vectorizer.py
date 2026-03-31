from transformers import BertTokenizer, BertModel
import torch

# charger tokenizer et modèle
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    # embeddings de la phrase (CLS token)
    cls_embedding = outputs.last_hidden_state[:, 0, :]

    return cls_embedding.squeeze().numpy()