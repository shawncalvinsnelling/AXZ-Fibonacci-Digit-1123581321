# Arbitrary-Precision Safety

The verifier uses Python integer arithmetic. Python integers are arbitrary precision subject to available memory.

For this finite universe, the maximum absolute final value is:

```text
1123581321
```

Its bit length is:

```text
31
```

The repository also includes a runtime guard that checks values greater than 2^64.
