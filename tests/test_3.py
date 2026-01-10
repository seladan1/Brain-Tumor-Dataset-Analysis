import pandas as pd
import pytest
from src.question_3 import calc_spearman_gender_survival


def test_perfect_positive_correlation():
    # Correlation should be 0.894, P-Value should be 0.1056.

    df = pd.DataFrame({"Gender": ["Female", "Female", "Male", "Male"], "Survival Time (months)": [10, 20, 30, 40]})

    corr, p_value = calc_spearman_gender_survival(df)

    assert corr == pytest.approx(0.894, abs=0.001)
    assert p_value == pytest.approx(0.1056, abs=0.001)


def test_no_correlation():
    # Correlation shoud be 0

    df = pd.DataFrame({"Gender": ["Male", "Female", "Male", "Female"], "Survival Time (months)": [10, 10, 20, 20]})

    corr, p_value = calc_spearman_gender_survival(df)

    assert corr == 0.0
    assert p_value == 1.0


def test_negative_correlation():
    # Correlation should be -0.894, P-Value should be 0.1056.

    df = pd.DataFrame({"Gender": ["Male", "Male", "Female", "Female"], "Survival Time (months)": [10, 20, 30, 40]})

    corr, p_value = calc_spearman_gender_survival(df)

    assert corr == pytest.approx(-0.894, abs=0.001)
    assert p_value == pytest.approx(0.1056, abs=0.001)

