from sampletest.add import add

def test_num():
    assert add(1, 2) == 3

def test_str():
    assert add("a", "b") == "ab"