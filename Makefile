tabFile = "./files/test.tab"

.PHONY: build
build:
	mkdir -p build
	cmake -DCMAKE_BUILD_TYPE=Release -B build .
	cmake --build build

.PHONY: clean
clean:
	rm -rf build

bench:
    ./build/sort --file=$(tabFile) --benchmark_out="data.json" --benchmark_out_format="json"