"""Module for handling Jupyterhub launch-demo functionality in the Syft theme."""

from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util import logging

logger = logging.getLogger(__name__)


class LaunchDemo(SphinxTransform):
    """Transform -launch- text to html anchor link."""

    default_priority = 500  # Priority of the transform

    def apply(self):
        """Launch demo on Jupyter Hub."""
        # Get the base URL for Jupyter Hub from conf.py
        jupyter_hub_url = self.app.config.jupyter_hub_url

        # Loop through all text nodes in the document
        for node in self.document.traverse(nodes.Text):
            if "-launch-" in node:
                # Get the document (notebook) path relative to the Sphinx source directory
                docname = (
                    self.env.docname
                )  # This gives you the current document path without the .rst or .md extension

                # Construct the full URL using jupyter_hub_url and the docname
                full_url = f"{jupyter_hub_url}/{docname}.ipynb"

                # Define the HTML code that will replace '-launch-'
                html = (
                    f'<div class="try--wrapper">'
                    f'<a href="{full_url}" class="try--this">'
                    f'<span class="try--text">Try This &#8599;</span>'
                    f"</a></div>"
                )

                # Replace the raw text node with the new HTML node
                new_node = nodes.raw("", html, format="html")
                node.parent.replace(node, new_node)

                logger.info(f"Replaced -launch- with the full URL: {full_url}")


def setup(app):
    """Apply launch demo on Jyputer Hub."""
    app.add_transform(LaunchDemo)
    # Register the new config value to be read from conf.py
    app.add_config_value("jupyter_hub_url", "", "env")
