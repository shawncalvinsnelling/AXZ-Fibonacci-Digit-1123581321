# Proof Sketch

## Statement

For the digit string `1123581321`, under the allowed grammar of fixed-order concatenation plus binary operations `+`, `-`, and `*`, with directional subtraction only, the full value universe contains every positive integer from `1` through `7972` and does not contain `7973`.

## Grammar

Every expression is an ordered binary tree over a partition of the digit string into nonempty contiguous substrings. A substring leaf evaluates to its base-10 integer value. For each split of an interval into left and right subintervals, the evaluator combines the already-certified left and right value sets with:

```text
A + B
A - B
A * B
```

The evaluator never adds the extra branch `B - A` for the same split.

## Exhaustiveness induction

Base case: each nonempty interval `D[i:j]` contains the concatenation leaf `int(D[i:j])`.

Inductive step: assume all values for strict subintervals have been exactly enumerated. Every legal parse tree for `D[i:j]` has a root split `k`, a left legal parse tree on `D[i:k]`, a right legal parse tree on `D[k:j]`, and one allowed binary operator. The recurrence enumerates every such split and every such pair of subvalues, so it includes every legal expression value. Conversely, every generated value is produced by a valid split, two valid subexpressions, and one allowed operator, so it is legal.

By induction over interval length, `V(0,10)` is exactly the legal universe.

## Finite certificate result

The verifier computes the exact full-universe set and checks:

- `len(V(0,10)) = 153,206`
- all integers `1..7972` are present
- `7973` is absent
- the sorted value-set hashes match the checked-in ledgers

## Boundary witness

```text
7972 = 1 - ((1 + 2) * (((3 - (5 + 81)) * 32) - 1))
```

## Scope boundary

Truth label: `CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES`.

This is a finite exact result for the stated grammar only. It does not claim to solve all digit-expression systems or any famous open problem.
