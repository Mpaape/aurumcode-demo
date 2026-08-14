# aurumcode-demo

A deliberately small service used to demonstrate [AurumCode](https://github.com/Mpaape/AurumCode)
reviewing pull requests automatically.

Every pull request opened here triggers `.github/workflows/code-review.yml`, which
runs AurumCode's security pass over the pull request's diff, publishes the findings
as a comment, and fails the check when a finding is severity `error` — so a pull
request that introduces a vulnerability cannot be merged green.

The security pass is deterministic: it matches the diff's added lines against an
embedded rule catalog and calls no model, so this demo needs no API key and no
repository secret.
