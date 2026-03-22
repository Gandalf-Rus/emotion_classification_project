import re
import emoji
import spacy

# try to load english spacy model, download if missing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# customize the stop words list to keep negations and important modifiers
exceptions = ['not', 'no', 'never', 'none', 'cannot', 'without', 'against', 'but', 'however', 'nothing']
for word in exceptions:
    nlp.vocab[word].is_stop = False

def clean_text_basic(text):
    """performs basic text cleaning using regular expressions and demojizes emojis."""
    text = str(text).lower()
    text = emoji.demojize(text, delimiters=(" ", " "))
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\[name\]', '', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def lemmatize_and_remove_stopwords(text):
    """lemmatization and removal of stop words using spacy."""
    doc = nlp(text)
    clean_tokens = []
    for token in doc:
        if not token.is_stop and token.text.strip():
            clean_tokens.append(token.lemma_.lower())
    return " ".join(clean_tokens)

def preprocess_text(text):
    """runs the complete text cleaning pipeline: 
    regex & emojis -> spacy lemmatization."""
    basic_cleaned = clean_text_basic(text)
    return lemmatize_and_remove_stopwords(basic_cleaned)