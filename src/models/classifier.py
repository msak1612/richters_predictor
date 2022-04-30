from pycaret.classification import setup
from pycaret.classification import create_model


class Classifier:

    def __init__(self, df) -> None:
        # For setup parameters, we referred to https://pycaret.readthedocs.io/en/latest/api/classification.html.
        # Based on the sparse data of binary fields for secondary use related features, we  ignore low variance
        # features.
        # Geo IDs are considered as cardinal data due to their range based values and does cardinal encoding.
        # In addition, pycaret does one hot encoding by default on remaining categorical features.
        # e.g. https://pycaret.gitbook.io/docs/get-started/preprocessing/data-preparation#one-hot-encoding
        self.clf = setup(data=df,
                         target='damage_grade',
                         session_id=123,
                         fold_shuffle=True,
                         use_gpu=True,
                         ignore_low_variance=True,
                         silent=True,
                         train_size=0.8,
                         numeric_features=[
                             'count_floors_pre_eq', 'count_families', 'age',
                             'area_percentage', 'height_percentage'
                         ],
                         categorical_features=[
                             'land_surface_condition', 'foundation_type',
                             'roof_type', 'ground_floor_type',
                             'other_floor_type', 'position',
                             'plan_configuration', 'legal_ownership_status'
                         ],
                         high_cardinality_features=[
                             'geo_level_1_id', 'geo_level_2_id',
                             'geo_level_3_id'
                         ],
                         ignore_features=['building_id'])

    def create_baseline_model(self):
        return create_model('lightgbm')

    def create_tuned_model(self):
        # Based on https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html,
        # the model is tuned for its hyperparameters.
        return create_model('lightgbm',
                            learning_rate=0.2,
                            n_estimators=250,
                            num_leaves=90,
                            reg_alpha=3,
                            reg_lambda=0.2)
