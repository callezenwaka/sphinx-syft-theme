# Sphinx Syft Theme

This is Sphinx Syft Theme package. You can contribute via
[Github](https://github.com/callezenwaka/sphinx-syft-theme/).


Run package locally [Run Local](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#packaging-your-project)
```
python3 -m pip install -e .
```

Run test
```
python -m unittest discover tests
```

Build package
```
pip install build
```

Build for sdist
```
python3 -m build --sdist
```

Build for wheel
```
python3 -m build --wheel
```

Check distribution
```
twine check dist/*
```

Upload distribution
```
twine upload dist/*
```

# Sphinx Syft Theme Documentation

Build files
```
jupyter-book build .
```

Build all files
```
jupyter-book build --all .
```

Build all doc files 
```
jupyter-book build --all ./docs
```

To delete the .jupyter_cache folder as well, add the --all flag like so
```
jupyter-book clean . --all
```

Install dependencies
```
pip install -r requirements.txt

```
