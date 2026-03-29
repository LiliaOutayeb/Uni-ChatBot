import json

def load_dataset(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def extract_pairs(data):
    pairs = []

    for intent in data['intents']:
        tag = intent['tag']
        patterns = intent['patterns']

        for pattern in patterns:
            pairs.append({
                "input": pattern,
                "label": tag 
            })

    return pairs
