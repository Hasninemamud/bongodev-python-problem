import pytest
from Pytest.sample3.sample import add

@pytest.mark.skip
def test_add_num():
    assert add(1 + 2) == 3

def test_add_str():
    assert add("a", "b") == "ab"