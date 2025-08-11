import os
import sys

from src.logger import logging
import numpy as np
import pandas as pd
from src.exception import CustomException
from sklearn.metrics import r2_score
import pickle


def save_object(file_path, obj):
    """
    Save the object to a file using pickle.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        raise CustomException(f"Error saving object: {str(e)}", sys) from e
    
def evaluate_model(x_train ,y_train ,x_test ,y_test, modeles):
    try:
        report={}
        for i in range(len(list(modeles))):
            model=list(modeles.values())[i]
            ##train the model
            model.fit(x_train,y_train)
            y_predict_train=model.predict(x_train)
            y_predict_test=model.predict(x_test)
            train_model_score=r2_score(y_train,y_predict_train)
            test_model_score=r2_score(y_test,y_predict_test)

            report[list(modeles.keys())[i]] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e,sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)