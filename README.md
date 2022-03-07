# Tracker

<a href="https://github.com/guemax/tracker/issues" alt="Issues"><img src="https://img.shields.io/github/issues/guemax/tracker"></a>
<a href="https://github.com/guemax/tracker/pulls" alt="Pull requests"><img src="https://img.shields.io/github/issues-pr/guemax/tracker"><a>
<a href="https://github.com/guemax/tracker" alt="Code coverage"><img src="./docs/coverage-badge/coverage.svg"></a>
<a href="https://github.com/guemax/tracker/blob/main/LICENSE" alt="License"><img src="https://img.shields.io/github/license/guemax/tracker"></a>

<!-- ![GitHub release (latest by date)](https://img.shields.io/github/v/release/guemax/tracker) -->

A command-line tool to track your computer usage time.

## Upcoming features

- _~~Start timer~~_ [2022-01-04]
- _~~Stop timer~~_ [2022-01-05]
- _~~Add description of done work when stopping the timer~~_ [2022-01-05]
- _~~Show old entries grouped by date~~_ [2022-01-08]
- _~~Show old entries of a specific day~~_ [2022-01-15]
- Show summary of a day
- Show number of hours per day/week

## Priority of features

P1

- [x] Start timer
- [x] Stop timer
- [x] Add description of done work

P2

- [x] Show old entries grouped by date
- [X] Show old entries of a specific day

P3

- [ ] Show summary of a day
- [ ] Show number of hours per day/week

## Contributing

Downlaod the source code and move into the root directory of the project. Use `python3 -m src.main` to run Tracker. Append the command you would like to execute, for example `python3 -m src.main start` to start a timer.
  
On Linux (or if you have `make` installed, you can use some commands which are useful for developing:

```bash
# Clean the project: Removes old entries and the log file
make clean

# Run the tests to verify you did not broke something while writing some code
make test

# Setup some test entries for developing
make setup

# Show coverage information
make coverage

# Build the coverage badge for the README
make badge
```

If you want to contribute to the project, please submit your ideas through a pull request. Make sure you code follows Python's PEP8 style guides and that all tests pass. If you are adding a new feature, it is good to write some tests for that one.
