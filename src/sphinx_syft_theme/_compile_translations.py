"""Generate compiled static translation assets for Sphinx."""

import json
import os
import subprocess
from pathlib import Path

# In case the smodin.io code is different from the Sphinx code
RENAME_LANGUAGE_CODES = {
    "zh-cn": "zh_CN",
    "zh-tw": "zh_TW",
}


def convert_json(folder=None):
    """Convert JSON translations into .mo/.po files for Sphinx.

    folder:
        the source folder of the JSON translations. This function will put the
        compiled .mo/.po files in a specific folder relative to this source
        folder. This parameter is just provided to make testing easier.
    """
    # Raw translation JSONs that are hand-edited
    folder = folder or Path(__file__).parent / "assets" / "translations"
    # Location of compiled static translation assets
    out_folder = folder / ".." / ".." / "theme" / "sphinx_syft_theme" / "static"

    # compile po
    for path in (folder / "jsons").glob("*.json"):
        data = json.loads(path.read_text("utf8"))
        assert data[0]["symbol"] == "en"
        english = data[0]["text"]
        for item in data[1:]:
            language = item["symbol"]
            if language in RENAME_LANGUAGE_CODES:
                language = RENAME_LANGUAGE_CODES[language]
            out_path = (
                out_folder / "locales" / language / "LC_MESSAGES" / "syfttheme.po"
            )
            if not out_path.parent.exists():
                out_path.parent.mkdir(parents=True)
            if not out_path.exists():
                header = f"""
msgid ""
msgstr ""
"Project-Id-Version: Sphinx-Syft-Theme\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Language: {language}\\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\\n"
"""
                out_path.write_text(header)

            with out_path.open("a") as f:
                f.write("\n")
                f.write(f'msgid "{english}"\n')
                text = item["text"].replace('"', '\\"')
                f.write(f'msgstr "{text}"\n')

    # compile mo
    for path in (out_folder / "locales").glob("**/syfttheme.po"):
        subprocess.check_call(
            [
                "msgfmt",
                os.path.abspath(path),
                "-o",
                os.path.abspath(path.parent / "syfttheme.mo"),
            ]
        )


if __name__ == "__main__":
    print("[SBT]: Compiling translations")
    convert_json()
