# Chatbot NLP Project

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

## Version 1 : Vectorisation avec word2vec

Dans main.py, décommentez la partie word2vect et commentez le reste

## Version 2 : Vectorisation avec BERT

Dans main.py décommentez la partie BERT et commentez le reste

## Version 3 : Vectorisation avec Glove

Dans main.py Décommentez la partie GLOVE et commentez le reste

### Lancer :

```bash
python main.py
```

Au premier lancement il est possible d'obtenir ce warning :

```bash
Warning: You are sending unauthenticated requests to the HF Hub
```

Ce n'est pas une erreur, le code fonctionne normalement tout de même.
Cependant, il est possible de supprimer le warning :

- Creer un compte HuggingFace
- Generer un token
- Executer la commande suivante dans le terminal :

```bash
huggingface-cli login [token genéré]
```

Lors du chargement du modèle GloVe avec gensim, l’erreur suivante peut apparaître :

```bash
ssl.SSLCertVerificationError: certificate verify failed
```

Cette erreur est liée à une mauvaise configuration des certificats SSL sur l’environnement local (Windows + Python), empêchant le téléchargement du modèle depuis Internet.
Pour contourner ce problème, la vérification SSL a été désactivée dans glove_vectorizer.py :

```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

Cette solution est **temporaire** car elle desactive la securité HTTPS.

---

### TO BE CONTINUED
