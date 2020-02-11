.PHONY: build
build:
	mkdir -p build
	cmake -DCMAKE_BUILD_TYPE=Release -B build .
	cmake --build build

.PHONY: clean
clean:
	rm -rf build
