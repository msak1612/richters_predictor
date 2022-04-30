from pycaret.classification import plot_model

# This function analyzes the performance of a trained model with 
# plot/estimator as ‘class_report’ - Classification Report
def plot_report(model):
    plot_model(model, 'class_report')

# This function analyzes the performance of a trained model with 
# plot/estimator as ‘confusion_matrix’ - Confusion Matrix
def plot_confusion_matrix(model):
    plot_model(model, 'confusion_matrix')

# This function analyzes the performance of a trained model with 
# plot/estimator as ‘feature_all’ - Feature Importance (All)
def plot_feature_importance(model):
    plot_model(model, 'feature_all')
