import pandas as pd
import os


def load_data(file_path : str) -> pd.DataFrame :
    """ 
      Loads csv data into a pandas DataFrame.

      Args : 
        file_path (str): Path to the CSV file.

      Returns :
        pd.DataFrame : loaded dataset.    
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at :{file_path}")

    return pd.read_csv(file_path)