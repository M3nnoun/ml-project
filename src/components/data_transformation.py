import sys
import os
import dataclasses

# from sklearn.discriminant_analysis import StandardScaler
from sklearn.impute import SimpleImputer

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler , OneHotEncoder

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object


## adding the config
@dataclasses.dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        """
        This function is responsible for creating a preprocessor object that will be used to transform the data.
        It handles both numerical and categorical columns by applying appropriate transformations.
        """
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipline=Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            cat_pipeline =Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('onehotencoder',OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical columns scaling and categorical columns encoding completed")
            preprocessor =ColumnTransformer(
                transformers=[
                    ('num',num_pipline, numerical_columns),
                    ('cat', cat_pipeline,categorical_columns)
                ]
            )
            logging.info("Preprocessor object created successfully")
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data transformation initiated")
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Data loaded successfully")
            preprocessor = self.get_data_transformer_object()
            target_column = "math_score"
            numerical_columns = ["writing_score", "reading_score"]
            input_feature_train = train_data.drop(columns=[target_column], axis=1)
            target_feature_train = train_data[target_column]
            ## do the same for the test data
            input_feature_test = test_data.drop(columns=[target_column], axis=1)
            target_feature_test = test_data[target_column]
            logging.info("Data transformation completed")
            
            ##tranform the dataframe
            input_feature_train_arr= preprocessor.fit_transform(input_feature_train)
            ## for the test we use defrent methode => .transform
            input_feature_test_arr= preprocessor.transform(input_feature_test)
            
            train_arr= np.c_[
                input_feature_train_arr , np.array(target_feature_train)
            ]
            test_arr= np.c_[
                input_feature_test_arr , np.array(target_feature_test)
            ]
            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)