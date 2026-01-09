import pytest
import pandas as pd
from src.clean_data import load_data, clean_data

def test_load_data_invalid_path():
    """Verify that the loader gracefully handles non-existent files."""
    assert load_data("non_existent.csv") is None

def test_age_empty():
    empty_df = pd.DataFrame(columns=['Age', 'Survival Time (months)'])
    # אנחנו מצפים שזה יעלה שגיאה או יחזיר פלט ריק, תלוי בהתנהגות הרצויה
    with pytest.raises(Exception):
        clean_data(empty_df)