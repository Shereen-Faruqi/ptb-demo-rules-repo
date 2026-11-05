# Team rules

Every pull request is checked against these five rules.

1. **No secrets in code.** API keys, passwords and tokens must not be written into the code. Read them from the environment instead.
2. **Docstrings.** Every new function has a docstring that says what it does.
3. **No leftover debug prints.** Debug `print` statements must be removed before merging.
4. **Tests travel with code.** A change to code under `shop/` must include a change to a test under `tests/` in the same pull request.
5. **Parameterised queries.** Database queries must pass values as parameters. Building SQL by joining strings is not allowed.

A change to this file needs a person to approve it.
