# pype

A Perl-like one-liner processor for Python. Write quick command-line data transformations using Python syntax with the convenience of Perl's `-n`, `-p`, and `-a` flags.

## Features

- **Line-by-line processing** with automatic input handling
- **Auto-split mode** for easy field extraction
- **Flexible module imports** with aliasing support
- **Code generation** mode for debugging and learning
- Familiar interface for anyone who has used Perl one-liners

## Installation

### pip

```bash
pip install pype-bin
```

### Nix

```bash
# Run directly
nix run github:conao3/python-pype

# Install to profile
nix profile install github:conao3/python-pype
```

## Quick Start

```bash
# Print each line with line numbers
cat file.txt | pype -n -e 'print(NR, line)' | python

# Convert to uppercase
cat file.txt | pype -n -l -e 'print(line.upper())' | python

# Extract the second field from space-separated data
echo "a b c" | pype -n -a -e 'print(F[1])' | python
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

### Built-in Variables

| Variable | Description |
|----------|-------------|
| `line` | Current line content |
| `L` / `_` | Alias for `line` |
| `NR` | Line number (1-indexed, available with `-n`) |
| `words` / `F` | Split fields (available with `-a`) |

## Examples

### Basic Line Processing

Print each line:

```bash
cat file.txt | pype -n -e 'print(line)' | python
```

Print with line numbers:

```bash
cat file.txt | pype -n -e 'print(NR, line)' | python
```

### Text Transformation

Convert to uppercase:

```bash
cat file.txt | pype -n -l -e 'print(line.upper())' | python
```

### Field Extraction

Print the second field (space-separated):

```bash
echo "a b c" | pype -n -a -e 'print(F[1])' | python
```

Use a custom separator:

```bash
echo "a:b:c" | pype -n -a -F: -e 'print(F[1])' | python
```

### Working with Modules

Parse JSON:

```bash
echo '{"a": 1}' | pype -m json -e 'print(json.loads(line))' | python
```

### Debugging

View the generated Python code:

```bash
echo "hello" | pype -n -l -p -c
```

## License

See [LICENSE](LICENSE) for details.
