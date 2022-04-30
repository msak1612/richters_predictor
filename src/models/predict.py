from pycaret.classification import predict_model


# Predicts Target & Score (probability of predicted class) using a trained model,
# then save the prediction in csv file.
def predict_and_store_result(model, data):
    pred = predict_model(model, data=data, raw_score=True, verbose=False)
    building_id = pred['building_id']
    tmp_score = pred.filter(['Score_0', 'Score_1', 'Score_2'])
    pred['damage_grade'] = tmp_score.idxmax(1)
    pred['building_id'] = building_id
    pred.replace(to_replace=['Score_0', 'Score_1', 'Score_2'],
                 value=[1, 2, 3],
                 inplace=True)
    pred.to_csv("../data/processed/result.csv",
                columns=['building_id', 'damage_grade'],
                index=False)