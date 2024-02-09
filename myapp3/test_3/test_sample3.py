import pytest
from myapp3.sample_3.sample import add
@pytest.mark.skip(reason= "just want to skip")
def test_add_num():
    assert add(1, 2) == 4
def test_add_str():
    assert add("a", "b") == "ab"
