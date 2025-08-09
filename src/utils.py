import os
import sys

from src.logger import logging
import numpy as np
import pandas as pd
from src.exception import CustomException

def save_object(file_path, obj):
    """
    Save the object to a file using pickle.
    """
    import pickle
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        raise CustomException(f"Error saving object: {str(e)}", sys) from e