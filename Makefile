build_ext:
	python3 setup.py build_ext --inplace

sdist:
	python3 setup.py sdist

test_sdist:
	python3 setup.py sdist
	python3 -m twine upload --repository testpypi dist/*

clean:
	rm -rf *.out *.bin *.exe *.o *.a *.so test build dist
