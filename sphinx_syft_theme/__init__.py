__version__ = '0.0.0'

import os
import shutil
from pathlib import Path
from pkg_resources import get_distribution, DistributionNotFound

from bs4 import BeautifulSoup
from sphinx.application import Sphinx

from .components.banner import Banner
from .components.symoji import Symoji, convert_shortcodes_to_emojis, recursive_convert_shortcodes_to_emojis

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = "0.0.0"


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(Path(__file__).parent)
    return theme_path


def copy_config_images(app):
    if hasattr(app.config, "html_theme_options"):
        config = app.config.html_theme_options
    else:
        return

    if "footer_logos" in config:
        logos_config = config["footer_logos"]

        for key in logos_config:
            is_dict = isinstance(logos_config[key], dict)

            image = logos_config[key].get("image", "") if is_dict else logos_config[key]
            if image:
                image = copy_image(app, image)
            else:
                continue

            if is_dict:
                logos_config[key]["image"] = image
            else:
                logos_config[key] = image


def add_functions_to_context(app, pagename, templatename, context, doctree):
    def _denest_sections(html):
        soup = BeautifulSoup(html, "html.parser")
        sections = []
        for h1 in soup.find_all(["h1"]):
            sections.append(h1.parent)
            for child in h1.parent.children:
                if (child.name == "section") or (
                    child.name == "div" and "section" in child["class"]
                ):
                    sections.append(child.extract())
        return "\n".join(str(s) for s in sections)

    def apply_denested_layout(html):
        _html = _denest_sections(html)
        soup = BeautifulSoup(_html, "html.parser")

        # Insert Bootstrap classes into section divs
        for s in soup.select("section,div.section"):
            h = s.find(["h1", "h2", "h3", "h4", "h5", "h6"])
            if not h:
                continue

            i = h.name[-1]

            h["class"] = [f"display-{i}"] + h.get("class", [])

            if h.name in ["h1", "h2"]:
                s.wrap(
                    soup.new_tag(
                        "div", **{"class": f"container-fluid sectionwrapper-{i}"}
                    )
                )
                s.wrap(soup.new_tag("div", **{"class": f"container section-{i}"}))

            if h.name == "h2":
                h.wrap(soup.new_tag("div", **{"class": "section-title-wrapper"}))
                h.wrap(soup.new_tag("div", **{"class": "section-title"}))

        # Process banner tags and modify section div styles
        for s in soup.find_all("banner"):
            image = s.get("image", None)
            color = s.get("color", None)
            caption = s.get("caption", None)
            classes = s.get("class", None)

            d = s.find_parent("div", ["section"])
            if d is not None and classes is not None:
                d["class"] += classes

            d = s.find_parent("div", ["sectionwrapper-1", "sectionwrapper-2"])
            s.extract()
            if d is None:
                continue

            if image:
                image = copy_image(app, image)

            if image and color:
                style = (
                    f"background-image: linear-gradient({color},{color}), url({image});"
                )
            elif image:
                style = f"background-image: url({image});"
            elif color:
                style = f"background-color: {color};"
            else:
                style = None

            if style:
                d["style"] = style

            if caption:
                cd = soup.new_tag("div", **{"class": "section-banner-caption"})
                cd.string = caption
                d.append(cd)

        return str(soup)

    context["apply_denested_layout"] = apply_denested_layout

    def spt_pathto(uri):
        baseuri, anchor = uri.split("#", 1) if "#" in uri else (uri, "")
        anchor = "#" + anchor if anchor else ""
        if context["hasdoc"](baseuri):
            docuri = context["pathto"](baseuri)
            return docuri.split("#", 1)[0] + anchor
        else:
            return uri

    context["spt_pathto"] = spt_pathto

    if 'body' in context:
        context['body'] = convert_shortcodes_to_emojis(context['body'])

    if 'secondary_sidebar_items' in context:
        context['secondary_sidebar_items'] = [
            convert_shortcodes_to_emojis(item) for item in context['secondary_sidebar_items']
        ]

    if 'page_toc' in context:
        context['page_toc'] = convert_shortcodes_to_emojis(context['page_toc'])

    # Process secondary_sidebar_items if they include page_toc
    if 'secondary_sidebar_items' in context:
        context['secondary_sidebar_items'] = recursive_convert_shortcodes_to_emojis(context['secondary_sidebar_items'])


    # **Additional context update for sidebar templates (optional):**
    # If you have a specific way to identify sidebar templates (e.g., by templatename)
    # you can add a dedicated conversion step for those templates here.
    # For example:
    # if templatename == "page-toc.html":  # Replace with your actual template names
    #     content = context.get("content")  # Assuming sidebar content is stored as "sidebar" in context
    #     if content:
    #         context["content"] = convert_shortcodes_to_emojis(content)
    # return None  # This function doesn't need to return anything

def copy_image(app, image):
    conf_dir = Path(app.confdir)
    out_dir = Path(app.outdir)
    old_img = conf_dir / image
    if old_img.is_file():
        new_dir = out_dir / "_images"
        os.makedirs(new_dir, exist_ok=True)
        new_img = Path(new_dir) / old_img.name
        shutil.copy(old_img, new_img)
        return str(Path("_images") / old_img.name)
    else:
        raise FileNotFoundError(f"Image file not found: {old_img}")


def setup(app: Sphinx):
    # app.require_sphinx("5.0.2")
    app.add_html_theme("sphinx_syft_theme", get_html_theme_path())
    app.add_transform(Symoji)
    app.add_directive("banner", Banner)
    app.connect("builder-inited", copy_config_images)
    app.connect("html-page-context", add_functions_to_context)

    app.config.templates_path.append("_templates")

    return {
        "version": "0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
