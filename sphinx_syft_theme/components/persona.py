# sphinx_syft_theme/components/persona.py:

import re
from pathlib import Path
from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util.nodes import get_prev_node

SHORTCODE_TO_IMAGE = {}

def set_shortcode_to_image(shortcode_to_image):
    global SHORTCODE_TO_IMAGE
    SHORTCODE_TO_IMAGE = shortcode_to_image

def convert_shortcodes_to_nodes(text):
    pattern = re.compile(r'(\|\:\w+?\:\|)')
    parts = pattern.split(text)
    result = []

    for part in parts:
        if part in SHORTCODE_TO_IMAGE:
            image_path = SHORTCODE_TO_IMAGE[part]
            image_node = nodes.image(uri="_images/" + Path(image_path).name, alt=part, classes=['custom-emoji'])
            result.append(image_node)
        else:
            result.append(nodes.Text(part))
    
    return result

def recursive_convert_shortcodes_to_emojis(node):
    if isinstance(node, nodes.Text):
        new_nodes = convert_shortcodes_to_nodes(node.astext())
        node.parent.replace(node, new_nodes)
    elif isinstance(node, nodes.Element):
        for child in node.children:
            recursive_convert_shortcodes_to_emojis(child)

# def check_and_insert_image(node):
#     if isinstance(node, nodes.section):
#         prev_sibling = node.prev_sibling
#         if isinstance(prev_sibling, nodes.Text):
#             for shortcode in SHORTCODE_TO_IMAGE:
#                 if shortcode in prev_sibling.astext():
#                     image_path = SHORTCODE_TO_IMAGE[shortcode]
#                     image_node = nodes.image(uri="_images/" + Path(image_path).name, alt=shortcode, classes=['custom-emoji'])
#                     node.insert(0, image_node)
#                     break


def check_and_insert_image(node):
    if isinstance(node, nodes.section):
        prev_node = node
        while prev_node:
            prev_node = get_prev_node(prev_node)
            if isinstance(prev_node, nodes.Text):
                text = prev_node.astext()
                for shortcode in SHORTCODE_TO_IMAGE:
                    if shortcode in text:
                        image_path = SHORTCODE_TO_IMAGE[shortcode]
                        image_node = nodes.image(uri="_images/" + Path(image_path).name, alt=shortcode, classes=['custom-emoji'])
                        node.insert(0, image_node)
                        break
                break

class Persona(SphinxTransform):
    default_priority = 211

    def apply(self):
        for node in self.document.traverse(nodes.Element):
            recursive_convert_shortcodes_to_emojis(node)
            check_and_insert_image(node)