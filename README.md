# AXZ Fibonacci Digit No-Division Ordered Arithmetic Gap

This repository is a finite exact computational proof for the ordered digit sequence:

```text
1 1 2 3 5 8 1 3 2 1
```

Source note: Fibonacci-derived digit string from the blocks `1, 1, 2, 3, 5, 8, 13, 21`, flattened into `1123581321`.

## Theorem

Under the stated rules, every positive integer from 1 through **7972** is representable, and the first missing positive integer is:

```text
7973
```

## Rules

- Digit sequence: `1 1 2 3 5 8 1 3 2 1`.
- Each digit position is used exactly once.
- Digits must remain in order.
- Concatenation is allowed.
- Allowed operations: `+`, `-`, `*`.
- Parentheses are allowed through all ordered binary expression trees.
- Subtraction is directional: left subtree minus right subtree only.
- Division, powers, factorials, square roots, decimals, logs, hidden constants, and digit reordering are forbidden.

## Dynamic-programming recurrence

Let `D = 1123581321`.

For each interval `D[i:j]`, define `V(i,j)` as the set that starts with the concatenation leaf `int(D[i:j])`, then combines all left/right split values using the allowed operators.

The full universe is `V(0,10)`.

## Certificate

- Possible cut patterns: **512**
- Unique integer values generated: **153,206**
- Positive integer values generated: **86,139**
- Non-positive integer values generated: **67,067**
- Negative integer values generated: **67,066**
- Zero present: **true**
- Consecutive positive integers from 1: **7,972**
- First missing positive integer: **7,973**
- Minimum integer value: **-123,581,320**
- Maximum integer value: **1,123,581,321**

## Boundary witness

```text
7972 = 1 - ((1 + 2) * (((3 - (5 + 81)) * 32) - 1))
```

The integer `7973` is absent from the exact dynamic-programming value set.

## Reproduce locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
export PYTHONPATH="$PWD/src"      # Windows PowerShell: $env:PYTHONPATH="$PWD/src"

python scripts/verify_runtime_safety.py
python scripts/verify_challenge_4.py
python scripts/verify_data_hashes.py
python -m pytest -q
```

## Hashes

All-values SHA-256:

```text
29e1c35a2e8ad9faf16e872d236ad8bc74ae69d6ffa26a1d06d2dd230a955785
```

Positive-values SHA-256:

```text
10d0ce331835c2df349068385db42a8f76b9a03ef69ae9269895bb8262b99d80
```

Non-positive-values SHA-256:

```text
0782c6d92e42b4010fac83c9a6f36706b280b279a8c1912791d4c6fb8fa7a508
```

Negative-values SHA-256:

```text
23d285881832cc2ccd5d9429efe03138ffdbdd45e87f63d34491a05a86eab025
```

All-interval-values SHA-256:

```text
29e1c35a2e8ad9faf16e872d236ad8bc74ae69d6ffa26a1d06d2dd230a955785
```

## Truth label

```text
CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES
```

This repository proves only this finite ordered-expression universe under the exact stated rules.
