import pandas as pd

def load_data(file_path):
    """
    Loads a dataset from a CSV file.
    
    param file_path: The string path to the CSV file.
    return: pd.DataFrame if loading is successful, None otherwise.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
    
def clean_data(df):
    df_cleaned = df.dropna(subset=['Gender', 'Survival Time (months)']).copy()
    return df_cleaned