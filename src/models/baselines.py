import joblib
import numpy as np

class BaselineSVC:
    """wrapper for the trained linear svc baseline models."""
    
    def __init__(self, model_path, task_type='multiclass'):
        self.model = joblib.load(model_path)
        self.task_type = task_type
        
    def predict(self, features):
        """returns hard class predictions."""
        return self.model.predict(features)
    
    def decision_function(self, features):
        """returns raw geometric distances (Z-scores)."""
        return self.model.decision_function(features)
    
    def predict_multi_label(self, features, threshold=0.0):
        """returns active classes for one-vs-rest (model b)."""
        if self.task_type != 'multilabel':
            raise ValueError("use predict_multi_label only for model b (emotions).")
            
        distances = self.decision_function(features)
        # return boolean mask of activated classes
        return (distances > threshold).astype(int)