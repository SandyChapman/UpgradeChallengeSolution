# Stale PRs Tool

## Installation

Install for usage using `pip`:

```bash
pip install .
```

If you wish to continue development, you can use the requirements.txt which will include `-e` flag to indicate editable installation:

```bash
pip install -r ./requirements.txt
```

## Usage

For complete usage details, run

```bash
python -m stale_prs -h
```

## Examples

```bash

# Show open PRs on the SandyChapman/upgrade_challenge repo:
python -m stale_prs -r 'SandyChapman/upgrade_challenge'

# Show open PRs on the SandyChapman/upgrade_challenge and SandyChapman/upgrade_challenge_2 repos:
python -m stale_prs -r 'SandyChapman/upgrade_challenge' 'SandyChapman/upgrade_challenge_2'

# Show open PRs older than 1 week on the SandyChapman/upgrade_challenge repo:
python -m stale_prs -a '1 week' -r 'SandyChapman/upgrade_challenge'

# Show open PRs with the bug label on the SandyChapman/upgrade_challenge repo:
python -m stale_prs -l bug -r SandyChapman/upgrade_challenge

# Show open PRs with the bug label on the SandyChapman/upgrade_challenge and SandyChapman/upgrade_challenge_2 repos:
python -m stale_prs -l bug -r SandyChapman/upgrade_challenge SandyChapman/upgrade_challenge_2

# Show open PRs with the bug label older than 6 hours on the SandyChapman/upgrade_challenge and SandyChapman/upgrade_challenge_2 repos:
python -m stale_prs -a '6 hours' -l bug -r SandyChapman/upgrade_challenge SandyChapman/upgrade_challenge_2

# Write open PRs to a file named output.json on the SandyChapman/upgrade_challenge and SandyChapman/upgrade_challenge_2 repos:
python -m stale_prs -o 'output.json' -r SandyChapman/upgrade_challenge SandyChapman/upgrade_challenge_2
```

## Testing

In order to test, install the package (likely in editable mode) and run via pytest:

```bash
pytest ./test
```
