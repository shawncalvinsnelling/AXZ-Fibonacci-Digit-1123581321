from axz_fibonacci_digit_1123581321.core import EXPECTED, compute_certificate, full_values


def test_certificate_matches_expected():
    assert compute_certificate() == EXPECTED


def test_frontier_and_first_missing():
    values = full_values()
    assert all(n in values for n in range(1, 7973))
    assert 7973 not in values
