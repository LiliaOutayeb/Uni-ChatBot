# Chatbot NLP Project 

---

## Installation

### 1. Créer un environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 2. Installation des dependances
```bash
pip install pandas nltk gensim scikit-learn transformers torch
```
### 3. Telecharger les ressources nltk
```bash
python download_nltk.py
```
### 4. Pipeline NLP

-> Nettoyage (regex)
-> Normalisation
-> Tokenization
-> POS Tagging
-> Lemmatisation
-> Vectorisation

## VERSION 1 : Vectorisation avec word2vec
Dans main.py, décommentez la partie word2vect et commentez la partie BERT

## Version 2 : Vectorisation avec BERT
Dans main.py décommentez la partie BERT et commentez la partie Word2vec

### Lancer :
```bash
python main.py
```

Au premier lancement il est possible d'obtenir ce warning :

```bash
Warning: You are sending unauthenticated requests to the HF Hub
```
Ce n'ai pas une erreur, le code fonctionne normalement tout de même, cependant,
il est possible de supprimer le warning :
  - Creer un compte HuggingFace
  - Generer un token
  - Executer la commande suivante dans le terminal :
    
```bash
huggingface-cli login [token generé]
```



---
### TO BE CONTINUED 
