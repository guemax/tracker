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