from axz_fibonacci_digit_1123581321.core import EXPECTED_HASHES, compute_hashes


def test_hashes_match_expected():
    assert compute_hashes() == EXPECTED_HASHES
