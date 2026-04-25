import joblib

class TextVectorizer:
    """handles loading and applying saved tf-idf vectorizers."""
    
    def __init__(self, vectorizer_path):
        self.vectorizer = joblib.load(vectorizer_path)
        
    def transform(self, texts):
        """transforms a list of raw strings into a sparse tf-idf matrix."""
        # texts should be preprocessed before passing here
        return self.vectorizer.transform(texts)