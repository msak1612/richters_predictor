from pycaret.classification import plot_model


def plot_report(model):
    plot_model(model, 'class_report')


def plot_confusion_matrix(model):
    plot_model(model, 'confusion_matrix')


def plot_feature_importance(model):
    plot_model(model, 'feature_all')
