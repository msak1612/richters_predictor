from pycaret.classification import evaluate_model

# This function analyzes the performance of a trained model with 
# plot/estimator as ‘class_report’ - Classification Report
def plot_report(model):
    evaluate_model(model)