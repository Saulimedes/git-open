# Git Repo Opener

This Python script allows users to quickly open Git/Hub pages for specific repositories, branches, commits, or issues directly from the command line. It's a handy tool for developers who frequently work with GitHub and prefer to manage their workflow through the command line.

## Features

- Open the GitHub page of a current repository
- Open specific branches, commits, or the issues page of a repository
- Can append a suffix to the URL
- Option to print the URL instead of opening it in a browser

## Requirements

- Python 3
- Git installed and configured
- Access to the terminal or command line interface

## Installation

No installation is required. Simply download the script and run it using Python.

## Usage

Run the script from the command line with optional arguments:

```
python git-open [options] [remote] [branch]
```

### Options

- `--commit`: Opens the current commit in the browser.
- `--issue`: Opens the issues page of the repository.
- `--suffix [SUFFIX]`: Appends a suffix to the URL (e.g., a specific file path).
- `--print`: Prints the generated URL instead of opening it in a browser.
- `remote`: Specifies the Git remote. Defaults to 'origin' if not provided.
- `branch`: Specifies the branch name. If not provided, the current branch is used.

### Examples

1. Open the current branch on GitHub:
   ```
   git-open
   ```

2. Open the issues page of the current repository:
   ```
   git-open --issue
   ```

3. Print the URL of the current commit without opening a browser:
   ```
   git-open --commit --print
   ```

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
