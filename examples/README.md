# One example per language AurumCode covers

Each directory holds a small file carrying the same four planted defects, so the
same pull request shows what the deterministic security pass catches in every
language — and, just as importantly, what it misses.

The pass is a regex matcher over the lines a change **adds**. It calls no model
and needs no credential, which is why this repository runs it with no secrets
configured. Four of the eight catalogued rules carry a matcher today
(`sql-injection`, `command-injection`, `hardcoded-secret`, `xss`); the command
announces that coverage on every run rather than implying it applied all eight.

## Measured coverage

Run against these exact files before this pull request was opened. A cross is a
real gap, not a rule that does not apply.

| Language | hardcoded-secret | sql-injection | command-injection | xss |
|---|:--:|:--:|:--:|:--:|
| JavaScript | yes | yes | yes | yes |
| Python | yes | yes | yes | — |
| C++ | yes | yes | yes | — |
| Go | yes | yes | **no** | — |
| C# | yes | yes | **no** | — |
| PowerShell | yes | yes | **no** | — |
| Bash | yes | **no** | **no** | — |
| Rust | **no** | **no** | **no** | — |

`—` means the rule does not apply to that language's example, not that it failed.

## What the gaps are, precisely

The matcher was written against the C, Python and Node spellings of each defect,
so it misses the idiomatic form elsewhere:

- **Go** — `exec.Command("sh", "-c", "ping "+host)` does not match. The pattern
  requires `exec` followed by `l` or `v` (`execl`, `execve`), the C spellings.
- **C#** — `Process.Start(...)` is not in the pattern at all.
- **PowerShell** — `Invoke-Expression` is not in the pattern at all.
- **Bash** — `eval "ping $1"` is not matched, and SQL built by shell
  interpolation (`"... '$1'"`) has no `+` for the SQL rule to anchor on.
- **Rust** — all three miss. `const KEY: &str = "..."` puts a type between the
  name and the `=`, which the secret rule does not expect; `"...".to_owned() +
  name` puts a method call between the quote and the `+`, which the SQL rule
  does not expect; and `Command::new("sh").arg(...)` matches no command pattern.

None of this is hidden by the tool at runtime: the review prints which rules it
applied, and a rule with no matcher never claims a clean file. But a gap nobody
wrote down is a gap nobody fixes, so it is written down here.

## Documentation, which is a separate matter

Documentation generation covers Go, Rust, C# and JavaScript with native parsers
— no external toolchain to install. Python, C++, Bash and PowerShell still route
through their own extractors. That coverage is independent of the table above:
a language can document well and match poorly, and Rust is exactly that case.
