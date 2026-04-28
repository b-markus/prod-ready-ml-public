import pandas as pd
import pytest
from pandas.testing import assert_series_equal

from animal_shelter import features


def test_check_is_dog():
    with pytest.raises(RuntimeError) as exception:
        features.check_is_dog(pd.Series(["dog", "cat", "frog"]))
    assert "Found pets that are not dogs or cats." in str(exception.value)


def test_check_has_name():
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = features.check_has_name(s)
    expected = pd.Series([True, True, False])

    assert_series_equal(result, expected)


def test_get_sex():
    good_outcomes = features.get_sex(pd.Series(["unknown", "Female", "Male"]))
    mask_non_binary = features.get_sex(pd.Series(["unknown", "Something", "Male"]))

    assert good_outcomes.str.lower().isin(["unknown", "female", "male"]).all()
    assert mask_non_binary.str.lower().isin(["unknown", "female", "male"]).all()
