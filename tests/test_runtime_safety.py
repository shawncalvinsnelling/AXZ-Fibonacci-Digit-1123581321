def test_arbitrary_precision_runtime():
    a = 2**130 + 123456789
    b = 2**97 + 987654321
    assert (a + b) - b == a
    assert (a * b) // b == a
    assert (a - b) + b == a
