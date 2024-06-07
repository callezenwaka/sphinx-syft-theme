import json
from docutils import nodes
from importlib import resources
from docutils.utils import new_document
from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import LoggingReporter

symoji_styles = {
    'symoji': {
        'source': 'https://unpkg.com/twemoji@latest/dist/twemoji.min.js',
        'libs': [
            'symoji.js',
            'symoji.css',
        ]
    },
}

# define
def load_symoji_codes():
    """
    Load emoji codes from the JSON file.

    This function tweaks some emojis to avoid Sphinx warnings when generating
    the documentation. See:

    - Original issue: https://github.com/sphinx-doc/sphinx/issues/8276
    - New issue: https://sourceforge.net/p/docutils/feature-requests/79/
    """
    fname = resources.files('sphinx_syft_theme') / 'symoji.json'
    with open(fname, encoding='utf-8') as fp:
        codes = json.load(fp)

    # Avoid unexpected warnings
    warning_keys = []
    for key, value in codes.items():
        if value.startswith("*"):
            warning_keys.append(key)
    for key in warning_keys:
        codes[key] = "\\" + codes[key]

    return codes

# Define emoji class
class Symoji(SphinxTransform):
    default_priority = 211

    def __init__(self, document, startnode=None):
        super().__init__(document, startnode)
        # self.parser = self.app.registry.create_source_parser(self.app, 'rst')
        self.rst_parser = self.app.registry.create_source_parser(self.app, 'rst')
        # self.md_parser = self.app.registry.create_source_parser(self.app, 'md')

    def apply(self):
        config = self.document.settings.env.config
        settings, source = self.document.settings, self.document['source']

        codes = load_symoji_codes()

        to_handle = (set(codes.keys()) -
                     set(self.document.substitution_defs))

        for ref in self.document.traverse(nodes.substitution_reference):
            refname = ref['refname']
            if refname in to_handle:
                text = codes[refname]

                doc = new_document(source, settings)
                doc.reporter = LoggingReporter.from_reporter(doc.reporter)
                # Determine the parser based on the file extension
                # self.parser.parse(text, doc)
                self.rst_parser.parse(text, doc)
                # if source.endswith('.md'):
                #     self.md_parser.parse(text, doc)
                # else:
                #     self.rst_parser.parse(text, doc)

                substitution = doc.next_node()
                # Remove encapsulating paragraph
                if isinstance(substitution, nodes.paragraph):
                    substitution = substitution.next_node()
                ref.replace_self(substitution)