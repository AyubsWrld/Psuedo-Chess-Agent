.PHONY: all build run clean

all: build run

# Build the virtual environment and install requirements
build:
	chmod +x build.sh;
	./build.sh;
	chmod +x tplay

run:
	./temp/bin/python3 main.py $(ARGS);

# Clean up and remove the virtual environment
clean:
	./build.sh clean;