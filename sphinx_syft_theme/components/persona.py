import re
from docutils import nodes
from sphinx.transforms import SphinxTransform
from docutils import nodes

 # Add custom images
SHORTCODE_TO_IMAGE = {
    '|:openmined1:|': '_static/images/openmined1.png',
    '|:openmined2:|': '_static/images/openmined2.gif',
    '|:openmined3:|': '_static/images/openmined3.gif',
    '|:openmined4:|': '_static/images/openmined4.svg',
}

# Define  
def convert_shortcodes_in_text(text):
    pattern = re.compile(r'(\|\:\w+?\:\|)')
    parts = pattern.split(text)
    result = []

    for part in parts:
        if part in SHORTCODE_TO_IMAGE:
            image_node = nodes.image(uri=SHORTCODE_TO_IMAGE[part], alt=part, classes=['custom-emoji'])
            result.append(image_node)
        else:
            result.append(nodes.Text(part))
    
    return result

def convert_shortcodes_to_nodes(node):
    if isinstance(node, nodes.Text):
        new_nodes = convert_shortcodes_in_text(node.astext())
        for new_node in new_nodes:
            node.parent.insert(node.parent.index(node), new_node)
        node.parent.remove(node)
    elif isinstance(node, nodes.Element):
        for child in list(node.children):  # Use a copy of the list for safe iteration
            convert_shortcodes_to_nodes(child)

class Persona(SphinxTransform):
    default_priority = 211

    def apply(self):
        convert_shortcodes_to_nodes(self.document)