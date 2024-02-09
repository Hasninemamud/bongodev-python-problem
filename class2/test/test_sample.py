import pytest

from class2.sample import validation_age

def test_validation_age_valid_age():
    validation_age(10)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cann't be less then 0"):
        validation_age(-1)
