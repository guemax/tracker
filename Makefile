entries ?= 4

all:
	@echo "Running Tracker"
	@python3 -m src.main
clean:
	@echo "Cleaning up Tracker files"
	@-rm tracker/files/*
log:
	@echo "Showing Tracker log file"
	@cat tracker/files/tracker.log
test: clean
	@echo "Running tests"
	@python3 -m unittest discover
setup: clean
	@echo "Setting up test values"
	@python3 -m tracker.setup_values_for_test_purposes -e ${entries}
coverage: clean
	@python3 -m coverage run --omit=/usr/*,*__init__.py -m unittest discover
	@python3 -m coverage report
	@python3 -m coverage html
badge: coverage
	@coverage-badge -o ./docs/coverage-badge/coverage.svg -f