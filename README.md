# csv-sanitizer

A project to identify CSV errors in input files to the UCLA Digital Library

# Initial Setup

Clone the repository, from a terminal enter:

`git clone https://github.com/UCLALibrary/csv-sanitizer.git`

# Install Required Tools

We'll need a few modules to get started, move into the repository directory and run `pip`

- `cd csv-sanitizer`
- `pip -r requirements.txt`

To install script hooks and confirm tools were correctly installed, from a terminal, enter:

- `pre-commit --version`
- `pre-commit install`
- `pre-commit run --all-files`

If the pre-commit checks correctly run, there should be no errors and `Passed` will be the result of each hook.
