entries ?= 4

all:
	@echo "Running Tracker"
	@python3 -m src.main
clean:
	@echo "Cleaning up Tracker files"
	@-rm src/files/*
log:
	@echo "Showing Tracker log file"
	@cat src/files/tracker.log
test: clean
	@echo "Running tests"
	@python3 -m unittest discover
setup: clean
	@echo "Setting up test values"
	@python3 -m src.setup -e ${entries}
coverage: clean
	@python3 -m coverage run --omit=/usr/*,*__init__.py -m unittest discover
	@python3 -m coverage report
	@python3 -m coverage html
badge: coverage
	@coverage-badge -o ./docs/coverage-badge/coverage.svg -f