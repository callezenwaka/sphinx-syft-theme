# Sphinx Syft Theme

This mini documentation contains the basic development and deployment steps for sphinx-syft-theme. Additional information is available [here](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#packaging-your-project). Furthermore, you can contribute via [Github](https://github.com/callezenwaka/sphinx-syft-theme/).

## Steps to develop and deploy package

Local package installation 
```
python3 -m pip install -e .
```

Optional: Install build package in the current environment
```
pip install build
```

Build sdist package
```
python3 -m build --sdist
```

Build wheel package
```
python3 -m build --wheel
```

Check build package
```
twine check dist/*
```

Upload build package
```
twine upload dist/*
```

## Steps to install and use package

Build files
```
jupyter-book build .
```

Build all files
```
jupyter-book build --all .
```

To delete the .jupyter_cache folder as well, add the --all flag like so
```
jupyter-book clean . --all
```

Install dependencies
```
pip install -r requirements.txt

```