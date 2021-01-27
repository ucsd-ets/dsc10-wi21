.PHONY: assign
assign:
	otter assign lecture.ipynb build data --no-export-cell --no-init-cell --no-check-all --no-run-tests
	rm -rf build/autograder/tests
	rm -rf build/student/tests
	rm -rf build/blank
	rm -rf build/filled
	mv build/student build/blank
	mv build/autograder build/filled


.PHONY: export-blank
export-blank: assign
	cd build/blank && zip export-blank.zip -r *
	mv build/blank/export-blank.zip ./build


.PHONY: export-filled
export-filled: assign
	cd build/filled && zip export-filled.zip -r *
	mv build/filled/export-filled.zip ./build


.PHONY: clean
clean:
	rm -rf build
