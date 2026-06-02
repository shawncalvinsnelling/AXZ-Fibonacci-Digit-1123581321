from __future__ import annotations

import json
from pathlib import Path

from axz_fibonacci_digit_1123581321.core import DIGITS, EXPECTED_HASHES, TRUTH_LABEL, compute_certificate

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    cert = {
        "repository": "AXZ-Fibonacci-Digit-1123581321",
        "challenge": "AXZ Fibonacci Digit No-Division Ordered Arithmetic Gap",
        "challenge_number": 4,
        "digit_sequence": DIGITS,
        "truth_label": TRUTH_LABEL,
        "certificate": compute_certificate(),
        "hashes": EXPECTED_HASHES,
    }
    out = ROOT / "certificates" / "generated_certificate.json"
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(f"PASS: wrote {out}")


if __name__ == "__main__":
    main()
