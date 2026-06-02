# Upload first

Create a new GitHub repository named:

```text
AXZ-Fibonacci-Digit-1123581321
```

Use this description:

```text
Finite exact certificate for the Fibonacci-derived ordered digit sequence 1123581321 under +, -, ×, concatenation, fixed order, and directional subtraction.
```

Leave GitHub's automatic README, .gitignore, and license options turned off. This package already includes them.

When uploading through the GitHub web UI, hidden files may not upload automatically. If you do not see `.github/workflows/verify.yml` and `.gitignore` after upload, create them manually using the visible backup files:

- `VISIBLE_GITHUB_ACTIONS_verify.yml`
- `VISIBLE_GITIGNORE.txt`

After the workflow is active, the Actions tab should show `Verify finite certificate`.
