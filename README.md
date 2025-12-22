# python-pype

A Perl-like one-liner processor for Python.

## Install

### pip

```bash
pip install pype-bin
```

### Nix

```bash
nix run github:conao3/python-pype
```

```bash
nix profile install github:conao3/python-pype
```

## Usage

```bash
cat input.txt | pype [options] | python
```

### Options

| Option | Description |
|--------|-------------|
| `-e CODE` | Execute Python code for each line |
| `-n` | Process input line by line (like Perl's `-n`) |
| `-l` | Automatically strip newlines from input |
| `-a` | Auto-split mode: split each line into `words` / `F` list |
| `-F SEP` | Specify field separator for `-a` |
| `-p` | Auto-print each line after processing (like Perl's `-p`) |
| `-0` | Use NUL character as line separator |
| `-m MODULE` | Import module (e.g., `-m json`, `-m os.path=p`, `-m pathlib[Path]`) |
| `-M MODULE` | Import all from module (e.g., `-M pathlib`) |
| `-c` | Print generated Python source code only (without execution) |

### Variables

| Variable | Description |
|----------|-------------|
| `line` | Current line content |
| `L` / `_` | Alias for `line` |
| `NR` | Line number (1-indexed, available with `-n`) |
| `words` / `F` | Split fields (available with `-a`) |

## Examples

Print each line:
```bash
cat file.txt | pype -n -e 'print(line)' | python
```

Print line numbers:
```bash
cat file.txt | pype -n -e 'print(NR, line)' | python
```

Convert to uppercase:
```bash
cat file.txt | pype -n -l -e 'print(line.upper())' | python
```

Sum numbers:
```bash
seq 10 | pype -n -e 'total = total + int(line) if "total" in dir() else int(line)' -e 'if NR == 10: print(total)' | python
```

Print second field:
```bash
echo "a b c" | pype -n -a -e 'print(F[1])' | python
```

Use custom separator:
```bash
echo "a:b:c" | pype -n -a -F: -e 'print(F[1])' | python
```

Use module:
```bash
echo '{"a": 1}' | pype -m json -e 'print(json.loads(line))' | python
```

Show generated code:
```bash
echo "hello" | pype -n -l -p -c
```
