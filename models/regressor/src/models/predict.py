import pandas as pd
from pycaret.regression import predict_model


def predict_and_store_result(model, data):
    pred = predict_model(model, data=data, verbose=False)
    pred['damage_grade'] = pd.cut(pred['Label'], bins=3, labels=False)+1
    tmp_score = pred.filter(['building_id', 'damage_grade'])
    pred.to_csv("../data/processed/result.csv",
                columns=['building_id', 'damage_grade'],
                index=False)