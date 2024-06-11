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
    '|:woman_technologist_medium_skin_tone:|': '👩🏽‍💻',
    # Add custom images
    # '|:openmined1:|': '<img src="static/images/openmined1.png" alt="openmined1 emoji">',
    # '|:openmined2:|': '<img src="static/images/openmined2.png" alt="openmined2 emoji">',
    # '|:openmined3:|': '<img src="static/images/openmined3.png" alt="openmined3 emoji">'
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

    def apply(self):
        for node in self.document.traverse(nodes.title):
            node.replace_self(nodes.title('', convert_shortcodes_to_emojis(node.astext())))
