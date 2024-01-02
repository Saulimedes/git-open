# git-open

`git-open` is a convenient command-line tool that allows you to quickly open web pages related to your Git repository in your default web browser. It supports various Git hosting platforms like GitHub, GitLab, Gitea, SourceHut, and self-hosted Git repositories.

## Features

- Open the web page of the current Git repository on supported hosting platforms.
- Access specific sections of the repository such as branches, commits, issues, and pull/merge requests.
- Compatible with public and self-hosted Git repositories.
- Simple and easy-to-use command-line interface.

## Prerequisites

- Python 3.x
- Git (should be installed and configured on your system)

## Installation

1. Clone this repository or download the `git-open` script.
2. Place the script in a directory included in your system's `PATH`.
3. Make the script executable:

   ```bash
   chmod +x git-open
   ```

## Usage

Navigate to a Git repository in your terminal and use the script with the following options:

- Open the main web page of the current repository:

  ```bash
  git-open
  ```

- Open the web page for the current branch:

  ```bash
  git-open --branch
  ```

- Open the web page for the current commit:

  ```bash
  git-open --commit
  ```

- Open the repository's issues page:

  ```bash
  git-open --issue
  ```

- Open the repository's pull/merge requests page:

  ```bash
  git-open --pr
  ```

- Print the URL instead of opening it in a browser:

  ```bash
  git-open --print
  ```

- Specify a different remote (default is 'origin'):

  ```bash
  git-open --remote upstream
  ```

## Supported Hosting Services

- GitHub
- GitLab
- Gitea
- SourceHut (sr.ht)
- Self-hosted Git instances (Note: Custom URL patterns for self-hosted instances may require adjustments in the script)

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
