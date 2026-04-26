import numpy as np
import joblib
from sklearn.base import BaseEstimator, TransformerMixin

class TextVectorizer:
    """handles loading and applying saved tf-idf vectorizers."""
    
    def __init__(self, vectorizer_path):
        self.vectorizer = joblib.load(vectorizer_path)
        
    def transform(self, texts):
        """transforms a list of raw strings into a sparse tf-idf matrix."""
        # texts should be preprocessed before passing here
        return self.vectorizer.transform(texts)
    

class MeanEmbeddingVectorizer(BaseEstimator, TransformerMixin):
    """
    transformer for converting text into a single dense vector by averaging
    the word embeddings of its constituent tokens. compatible with scikit-learn api.
    """
    def __init__(self, word_model):
        self.word_model = word_model
        self.vector_size = word_model.vector_size

    def fit(self, x, y=None):
        return self

    def transform(self, x):
        # x is expected to be an iterable of strings
        doc_vectors = []
        for text in x:
            words = str(text).split()
            word_vectors = []
            
            for word in words:
                if word in self.word_model:
                    word_vectors.append(self.word_model[word])
            
            if len(word_vectors) > 0:
                # compute the geometric centroid
                doc_vectors.append(np.mean(word_vectors, axis=0))
            else:
                # return a zero vector for entirely out-of-vocabulary texts
                doc_vectors.append(np.zeros(self.vector_size))
                
        return np.array(doc_vectors)