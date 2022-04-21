# Tracker

<a href="https://github.com/guemax/tracker/issues" alt="Issues"><img src="https://img.shields.io/github/issues/guemax/tracker"></a>
<a href="https://github.com/guemax/tracker/pulls" alt="Pull requests"><img src="https://img.shields.io/github/issues-pr/guemax/tracker"><a>
<a href="https://github.com/guemax/tracker" alt="Code coverage"><img src="./docs/coverage-badge/coverage.svg"></a>
<a href="https://github.com/guemax/tracker/blob/main/LICENSE" alt="License"><img src="https://img.shields.io/github/license/guemax/tracker"></a>

<!-- ![GitHub release (latest by date)](https://img.shields.io/github/v/release/guemax/tracker) -->

A command-line tool to track your computer usage time.

## Features

Tracker allows you to start a timer and stop it again providing a message describing what you have been doing.
You can also show old entries or summarize the entries.

## Contributing

Downlaod the source code and move into the root directory of the project. Use `python3 -m tracker` to run Tracker. 
Append the command you would like to execute, for example `python3 -m tracker start` to start a timer.

The simple script `make.py` has some commands which are useful for developing:

```bash
# Get a list of all commands supported by make.py
python3 -m make --help

# Clean the project (Removes all entries and the log file)
python3 -m make clean

# Run the tests to verify you did not broke something while writing some code
python3 -m make test

# Setup some test entries for developing (in this case twelve)
python3 -m make setup --entries 12

# Show coverage information in default webbrowser
python3 -m make coverage --webbrowser

# Generate coverage badge for README
python3 -m make coverage --badge

# Show the content of the log file
python3 -m make log

# Show number of code lines and comments written for this project
python3 -m make count
```

If you want to contribute to the project, please submit your ideas through a pull request. 
Make sure your code follows Python's PEP8 style guides and that all tests pass. If you are adding a new feature, 
it is good to write some tests showing the usage of it.
