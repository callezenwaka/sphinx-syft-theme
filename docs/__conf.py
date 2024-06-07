# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import subprocess
import sys

# -- Project information -----------------------------------------------------

author = "The OpenMined Community"
copyright = "2023"

# -- General configuration ---------------------------------------------------

exclude_patterns = ["**.ipynb_checkpoints", ".DS_Store", "Thumbs.db", "_build"]

# -- General configuration ---------------------------------------------------

pygments_style = "sphinx"

suppress_warnings = ["myst.domains"]

templates_path = ["_templates"]

# -- Extensions configuration ------------------------------------------------

extensions = [
    # "ablog",
    # "myst_parser",
    "myst_nb",
    "sphinx_click.ext",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_external_toc",
    "sphinx_inline_tabs",
    "sphinx_panels",
    "sphinx_tabs.tabs",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
]

bibtex_bibfiles = ["references/references.bib"]

comments_config = {"hypothesis": False, "utterances": False}

external_toc_exclude_missing = False
external_toc_path = "_toc.yml"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

jupyter_cache = ""
jupyter_execute_notebooks = "cache"
execution_allow_errors = False
execution_excludepatterns = []
execution_in_temp = False
execution_timeout = 30

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]
myst_substitutions = {"sub3": "My _global_ value!"}
myst_url_schemes = ["mailto", "http", "https"]

nb_output_stderr = "show"

nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.parsers.rst.directives.body.Sidebar"),
]

numfig = True

panels_add_bootstrap_css = False

# source_suffix = {
#     ".rst": "restructuredtext",
#     '.md': 'markdown',
# }

thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "repository_branch": "master",
}

use_jupyterbook_latex = True
use_multitoc_numbering = True

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_syft_theme"
html_logo = "images/dummy_logo_dark.svg"
html_title = "Syft Theme"
html_copy_source = True
html_sourcelink_suffix = ""
html_favicon = "images/favicon.ico"
html_last_updated_fmt = ""

html_sidebars = {
    "index": [],
    "standalone": [],
    "references/blog/*": [
        "sidebar-logo.html",
        "search-field.html",
        "postcard.html",
        "recentposts.html",
        "tagcloud.html",
        "categories.html",
        "archives.html",
        "sbt-sidebar-nav.html",
        "sbt-sidebar-footer.html",
    ],
}

html_static_path = ["_static"]

html_theme_options = {
    "github_url": "https://github.com/callezenwaka/syft-theme",
    "twitter_url": "https://twitter.com/openmined",
    "repository_url": "https://github.com/callezenwaka/syft-theme",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "notebook_interface": "classic",
        "thebe": True,
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "logo_only": True,
    "logo_link": "https://syftbook.readthedocs.io/",
    "show_toc_level": 2,
    "navbar_align": "left",
    "navbar_links": [
        {"name": "Documentation", "url": "index#documentation"},
    ],
    "external_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/callezenwaka/syft-theme",
        },
    ],
    "page_layouts": {
        "index": "page-banner.html",
        "standalone": "page-standalone.html",
    },
    "footer_logos": {
        "NCAR": {
            "image": "images/NCAR-contemp-logo-blue.svg",
            "url": "https://ncar.ucar.edu",
        },
        "Unidata": {
            "image": "images/Unidata_logo_horizontal_1200x300.svg",
        },
        "UAlbany": "images/UAlbany-A2-logo-purple-gold.svg",
    },
    "extra_navbar": ('Theme by <a href="https://openmined.org">OpenMined Syft Project</a>'),
}

blog_path = "references/blog"
blog_post_pattern = "references/blog/*.md"
blog_baseurl = "https://syftbook.readthedocs.io"
fontawesome_included = True
post_auto_image = 1
post_auto_excerpt = 2

# ==============================================================================

subprocess.run([sys.executable, "getreferences.py", "./references"])
