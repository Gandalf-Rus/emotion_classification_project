from sklearn.metrics import precision_recall_fscore_support, classification_report

def calculate_macro_metrics(y_true, y_pred):
    """returns macro precision, recall, and f1 score."""
    p, r, f, _ = precision_recall_fscore_support(y_true, y_pred, average='macro', zero_division=0)
    return {'precision': p, 'recall': r, 'f1': f}

def generate_report(y_true, y_pred, class_names):
    """prints a full classification report."""
    print(classification_report(y_true, y_pred, target_names=class_names, zero_division=0))

def compare_models(y_true, predictions_dict):
    """
    compares multiple models based on macro f1-score.
    predictions_dict format: {'LogReg': y_pred_lr, 'SVC': y_pred_svc}
    """
    results = {}
    for model_name, y_pred in predictions_dict.items():
        metrics = calculate_macro_metrics(y_true, y_pred)
        results[model_name] = metrics
        
    return results