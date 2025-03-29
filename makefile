# Mark targets as phony (always execute)
.PHONY: run

# Default target
all: build

# Build the virtual environment and install requirements
build:
	chmod +x build.sh;
	./build.sh;

run:
	echo $(ARGS)
	./temp/bin/python3 main.py $(ARGS);

# Clean up and remove the virtual environment
clean:
	./build.sh clean;