import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    # Create a Series with a NaN value
    series = pd.Series([1, 2, np.nan, 4])

    # Compute expected median
    median_value = series.median()

    # Apply function
    result = clean_column(series)

    # Assert no NaN values remain
    assert result.isna().sum() == 0

    # Assert the NaN was replaced with the median
    assert median_value in result.values


def test_compute_revenue():
    # Create sample data
    quantity = pd.Series([1, 2, 3])
    price = pd.Series([10, 20, 30])

    # Expected result
    expected = pd.Series([10, 40, 90])

    # Apply function
    result = compute_revenue(quantity, price)

    # Assert element-wise multiplication is correct
    assert result.equals(expected) 