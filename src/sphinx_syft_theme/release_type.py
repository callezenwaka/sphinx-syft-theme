"""Module for handling release type functionality in the Syft theme."""

from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util import logging

logger = logging.getLogger(__name__)


def create_icon_html(keyword, app):
    """Create icon html for the sidebar."""
    icon_class = f"icon-{keyword}"
    release_types = app.config.html_theme_options.get("release_types", {})
    title_text = release_types.get(keyword, "")

    return f'<abbr class="icon {icon_class}" title="{title_text}"><span class="visually-hidden">{keyword.capitalize()}</span></abbr>'


def create_notecard_html(keyword, title_text):
    """Create notcard html for the main content."""
    return (
        f'<section class="notecard {keyword}" id="sect1">'
        f"<p><strong>{keyword.capitalize()}:</strong> <strong>This is {title_text.lower()}</strong></p>"
        f"</section>"
    )


class ReleaseTypeTransform(SphinxTransform):
    """Transform release type keywords to HTML and add sidebar icons and notecards."""

    default_priority = 500  # Priority of the transform

    def apply(self):
        """Apply release type transformation."""
        # Get release types from theme configuration
        release_types = self.app.config.html_theme_options.get("release_types", {})
        release_keywords = self.app.config.html_theme_options.get(
            "release_keywords", []
        )
        # Loop through all section nodes in the document
        for node in self.document.traverse(nodes.section):
            title = node.children[0]

            # Check if title has '-beta-', '-experimental-', or '-deprecated-' keyword
            for keyword in release_keywords:
                if f"-{keyword}-" in title.astext():
                    self._replace_keyword(title, keyword, release_types)
                    break

    def _replace_keyword(self, title_node, keyword, release_types):
        """Replace keyword in title and add corresponding HTML elements."""
        title_text = release_types.get(keyword, "")

        # Remove the keyword from the title text
        new_title_text = title_node.astext().replace(f"-{keyword}-", "").strip()
        title_node.clear()
        title_node += nodes.Text(new_title_text)

        # Create the <abbr> element for the icon and add it after the title text
        abbr_html = create_icon_html(keyword, self.app)
        abbr_node = nodes.raw("", " " + abbr_html, format="html")
        title_node += abbr_node

        # Create the notecard div and add it below the header in the main content
        notecard_html = create_notecard_html(keyword, title_text)
        notecard_node = nodes.raw("", notecard_html, format="html")
        title_node.parent.insert(1, notecard_node)

        # Log the additions
        logger.info(f"Added {keyword} icon to title and notecard below.")
