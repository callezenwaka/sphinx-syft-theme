"""Module for handling release type functionality in the Syft theme."""

from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util import logging

logger = logging.getLogger(__name__)


class ReleaseTypeTransform(SphinxTransform):
    """Transform release type keywords to HTML and add sidebar icons."""

    default_priority = 500  # Priority of the transform

    def apply(self):
        """Apply release type transformation."""
        # Loop through all section nodes in the document
        for node in self.document.traverse(nodes.section):
            title = node.children[0]

            # Check if title has '-beta-', '-experimental-', or '-deprecating-' keyword
            if "-beta-" in title.astext():
                self._replace_keyword(
                    title, "beta", "icon-beta", "Beta. Subject to changes."
                )

            elif "-experimental-" in title.astext():
                self._replace_keyword(
                    title,
                    "experimental",
                    "icon-experimental",
                    "Experimental. Expect behavior to change.",
                )

            elif "-deprecating-" in title.astext():
                self._replace_keyword(
                    title,
                    "deprecating",
                    "icon-deprecating",
                    "Deprecating. Not-recommended for use.",
                )

    def _replace_keyword(self, title_node, keyword, icon_class, title_text):
        """Replace keyword in title and add corresponding HTML elements."""
        # Remove the keyword from the title
        title_node.replace_self(
            nodes.title("", title_node.astext().replace(f"-{keyword}-", "").strip())
        )

        # Create the <abbr> element for the sidebar
        abbr_html = (
            f'<abbr class="icon {icon_class}" title="{title_text}">'
            f'<span class="visually-hidden">{keyword.capitalize()}</span>'
            f"</abbr>"
        )
        abbr_node = nodes.raw("", abbr_html, format="html")
        title_node.parent.insert(0, abbr_node)

        # Create the notecard div and add it below the header in the main content
        notecard_html = (
            f'<div class="notecard {keyword}" id="sect1">'
            f"<p><strong>{keyword.capitalize()}:</strong> <strong>This is {title_text.lower()}</strong></p>"
            f"</div>"
        )
        notecard_node = nodes.raw("", notecard_html, format="html")
        title_node.parent.insert(1, notecard_node)

        # Log the additions
        logger.info(f"Added {keyword} span, sidebar icon, and notecard.")

    # def apply(self):
    #     """Apply release type transformation."""
    #     for node in self.document.traverse(nodes.section):
    #         title = node.children[0]
    #         if '-beta-' in title.astext():
    #             self._replace_keyword(title, 'beta', 'icon-beta', 'Beta. Subject to changes.')
    #         elif '-experimental-' in title.astext():
    #             self._replace_keyword(title, 'experimental', 'icon-experimental', 'Experimental. Expect behavior to change.')
    #         elif '-deprecating-' in title.astext():
    #             self._replace_keyword(title, 'deprecating', 'icon-deprecating', 'Deprecated. Not recommended for use.')

    # def _replace_keyword(self, title_node, keyword, icon_class, title_text):
    #     """Replace keyword in title and add corresponding HTML elements."""
    #     title_node.replace_self(nodes.title('', title_node.astext().replace(f'-{keyword}-', '').strip()))

    #     # Create the <abbr> element for the sidebar
    #     abbr_html = (
    #         f'<abbr class="icon {icon_class}" title="{title_text}">'
    #         f'<span class="visually-hidden">{keyword.capitalize()}</span>'
    #         f'</abbr>'
    #     )
    #     abbr_node = nodes.raw('', abbr_html, format='html')

    #     # Insert the icon after the header in the sidebar
    #     for section in title_node.parent.traverse(nodes.sidebar):
    #         print('section: ', section)
    #         if 'sidebar' in section.attributes['classes']:
    #             section.insert(1, abbr_node)
    #             break

    #     # Create the notecard div and add it below the header in the main content
    #     notecard_html = (
    #         f'<div class="notecard {keyword}" id="sect1">'
    #         f'<p><strong>{keyword.capitalize()}:</strong> <strong>This is {title_text.lower()}</strong></p>'
    #         f'</div>'
    #     )
    #     notecard_node = nodes.raw('', notecard_html, format='html')
    #     title_node.parent.insert(2, notecard_node)


# def setup(app):
#     """Setup release type transformation."""
#     app.add_transform(ReleaseTypeTransform)
#     logger.info("ReleaseTypeTransform setup complete.")
