import re
from docutils import nodes
from sphinx.transforms import SphinxTransform
from docutils import nodes
# from importlib import resources
from docutils.utils import new_document
from sphinx.util.docutils import LoggingReporter

SHORTCODE_TO_UNICODE = {
    '|:man_technologist:|': '👨‍💻',
    '|:man_technologist_dark_skin_tone:|': '👨🏿‍💻',
    '|:man_technologist_light_skin_tone:|': '👨🏻‍💻',
    '|:man_technologist_medium_dark_skin_tone:|': '👨🏾‍💻',
    '|:man_technologist_medium_light_skin_tone:|': '👨🏼‍💻',
    '|:man_technologist_medium_skin_tone:|': '👨🏽‍💻',
    '|:woman_technologist:|': '👩‍💻',
    '|:woman_technologist_dark_skin_tone:|': '👩🏿‍💻',
    '|:woman_technologist_light_skin_tone:|': '👩🏻‍💻',
    '|:woman_technologist_medium_dark_skin_tone:|': '👩🏾‍💻',
    '|:woman_technologist_medium_light_skin_tone:|': '👩🏼‍💻',
    '|:woman_technologist_medium_skin_tone:|': '👩🏽‍💻'
}

# def convert_shortcodes_to_emojis(text):
#     pattern = re.compile(r'\|:(\w+?):\|')
#     return pattern.sub(lambda match: SHORTCODE_TO_UNICODE.get(f'|:{match.group(1)}:|', match.group(0)), text)


def convert_shortcodes_to_emojis(text):
    pattern = re.compile(r'(\|\:\w+?\:\|)')
    return pattern.sub(lambda match: SHORTCODE_TO_UNICODE.get(match.group(1), match.group(1)), text)

def recursive_convert_shortcodes_to_emojis(item):
    if isinstance(item, str):
        return convert_shortcodes_to_emojis(item)
    elif isinstance(item, list):
        return [recursive_convert_shortcodes_to_emojis(sub_item) for sub_item in item]
    elif isinstance(item, dict):
        return {key: recursive_convert_shortcodes_to_emojis(value) for key, value in item.items()}
    return item

# Define symoji class
class Symoji(SphinxTransform):
    default_priority = 211

    def __init__(self, document, startnode=None):
        super().__init__(document, startnode)
        self.parser = self.app.registry.create_source_parser(self.app, 'rst')

    def apply(self):
        settings, source = self.document.settings, self.document['source']
        to_handle = (set(SHORTCODE_TO_UNICODE.keys()) - set(self.document.substitution_defs))

        for node in self.document.traverse(nodes.title):
            node.replace_self(nodes.title('', convert_shortcodes_to_emojis(node.astext())))

        for ref in self.document.traverse(nodes.substitution_reference):
            refname = ref['refname']
            if refname in to_handle:
                text = SHORTCODE_TO_UNICODE[refname]

                doc = new_document(source, settings)
                doc.reporter = LoggingReporter.from_reporter(doc.reporter)
                # Determine the parser based on the file extension
                self.parser.parse(text, doc)
                # self.rst_parser.parse(text, doc)
                # if source.endswith('.md'):
                #     self.md_parser.parse(text, doc)
                # else:
                #     self.rst_parser.parse(text, doc)

                substitution = doc.next_node()
                # Remove encapsulating paragraph
                if isinstance(substitution, nodes.paragraph):
                    substitution = substitution.next_node()
                ref.replace_self(substitution)
