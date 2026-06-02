# Directional Subtraction

The subtraction operator is non-commutative and directional.

For a split with left value `A` and right value `B`, the recurrence adds only:

```text
A - B
```

It does not add `B - A` for the same split.
