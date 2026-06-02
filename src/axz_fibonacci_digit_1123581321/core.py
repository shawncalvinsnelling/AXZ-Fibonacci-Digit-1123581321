"""Core exact verifier for AXZ-Fibonacci-Digit-1123581321."""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from pathlib import Path

DIGITS = "1123581321"
TRUTH_LABEL = "CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES"
EXPECTED = {'all_interval_unique_values_generated': 153206,
 'consecutive_positive_integers_from_1': 7972,
 'first_missing_positive_integer': 7973,
 'max_absolute_final_bit_length': 31,
 'max_value': 1123581321,
 'min_value': -123581320,
 'negative_integer_values_generated': 67066,
 'nonpositive_integer_values_generated': 67067,
 'positive_integer_values_generated': 86139,
 'possible_cut_patterns': 512,
 'unique_integer_values_generated': 153206,
 'zero_present': True}
EXPECTED_HASHES = {'all_interval_values_sha256': '29e1c35a2e8ad9faf16e872d236ad8bc74ae69d6ffa26a1d06d2dd230a955785',
 'all_values_sha256': '29e1c35a2e8ad9faf16e872d236ad8bc74ae69d6ffa26a1d06d2dd230a955785',
 'negative_values_sha256': '23d285881832cc2ccd5d9429efe03138ffdbdd45e87f63d34491a05a86eab025',
 'nonpositive_values_sha256': '0782c6d92e42b4010fac83c9a6f36706b280b279a8c1912791d4c6fb8fa7a508',
 'positive_values_sha256': '10d0ce331835c2df349068385db42a8f76b9a03ef69ae9269895bb8262b99d80'}


@lru_cache(maxsize=None)
def interval_values(i: int, j: int) -> frozenset[int]:
    """Return all values for DIGITS[i:j] under ordered +, -, * and concatenation."""
    if not (0 <= i < j <= len(DIGITS)):
        raise ValueError("interval must satisfy 0 <= i < j <= len(DIGITS)")

    out: set[int] = {int(DIGITS[i:j])}
    for k in range(i + 1, j):
        left = interval_values(i, k)
        right = interval_values(k, j)
        for a in left:
            for b in right:
                out.add(a + b)
                out.add(a - b)
                out.add(a * b)
    return frozenset(out)


def full_values() -> set[int]:
    return set(interval_values(0, len(DIGITS)))


def all_interval_values() -> set[int]:
    out: set[int] = set()
    for i in range(len(DIGITS)):
        for j in range(i + 1, len(DIGITS) + 1):
            out.update(interval_values(i, j))
    return out


def sorted_newline_sha256(values) -> str:
    payload = "".join(f"{int(v)}\n" for v in sorted(values)).encode("utf-8")
    return sha256(payload).hexdigest()


def consecutive_frontier(values: set[int]) -> int:
    n = 0
    while n + 1 in values:
        n += 1
    return n


def compute_certificate() -> dict[str, object]:
    values = full_values()
    positives = {v for v in values if v > 0}
    nonpositives = {v for v in values if v <= 0}
    negatives = {v for v in values if v < 0}
    all_intervals = all_interval_values()
    frontier = consecutive_frontier(values)
    max_abs = max(abs(v) for v in values)
    return {
        "possible_cut_patterns": 2 ** (len(DIGITS) - 1),
        "unique_integer_values_generated": len(values),
        "positive_integer_values_generated": len(positives),
        "nonpositive_integer_values_generated": len(nonpositives),
        "negative_integer_values_generated": len(negatives),
        "zero_present": 0 in values,
        "consecutive_positive_integers_from_1": frontier,
        "first_missing_positive_integer": frontier + 1,
        "min_value": min(values),
        "max_value": max(values),
        "max_absolute_final_bit_length": max_abs.bit_length(),
        "all_interval_unique_values_generated": len(all_intervals),
    }


def compute_hashes() -> dict[str, str]:
    values = full_values()
    return {
        "all_values_sha256": sorted_newline_sha256(values),
        "positive_values_sha256": sorted_newline_sha256(v for v in values if v > 0),
        "nonpositive_values_sha256": sorted_newline_sha256(v for v in values if v <= 0),
        "negative_values_sha256": sorted_newline_sha256(v for v in values if v < 0),
        "all_interval_values_sha256": sorted_newline_sha256(all_interval_values()),
    }


def read_int_file(path: str | Path) -> list[int]:
    return [int(line) for line in Path(path).read_text().splitlines() if line.strip()]
