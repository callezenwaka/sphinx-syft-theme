# Sphinx Syft Theme

This is Sphinx Syft Theme package. You can contribute via [Github](https://github.com/callezenwaka/sphinx-syft-theme/).

## Documentation description

This mini documentation contains the basic development and deployment steps for sphinx-syft-theme.
Additional information is available [here](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#packaging-your-project)

## Additional resources include

- Theme setup is decribed [Read more](https://sphinx-theme-builder.readthedocs.io/en/latest/filesystem-layout/#how-it-looks).
- Storing project metadata in pyproject.toml [Read more](https://peps.python.org/pep-0621/).
- Error index: [Read more](https://sphinx-theme-builder.readthedocs.io/en/latest/errors/#project-double-version-declaration).

## Install dependencies

```
pip install -r requirements.txt

```

Revert to CI deployment

[build-system]
requires = ["setuptools", "wheel", "setuptools_scm"]
build-backend = "setuptools.build_meta"

[project]
name = "sphinx-syft-theme"
description = "Bootstrap-based Sphinx theme from the syft community"
dynamic = ["version"]
authors = [
{name = "Callis Ezenwaka", email = "callisezenwaka@gmail.com"},
]
maintainers = [
{ name = "Callis Ezenwaka", email = "callisezenwaka@gmail.com" },
]

[tool.setuptools_scm]
version_scheme = "post-release"
local_scheme = "no-local-version"

[tool.setuptools_scm]
write_to = "src/sphinx_syft_theme/**init**.py"
