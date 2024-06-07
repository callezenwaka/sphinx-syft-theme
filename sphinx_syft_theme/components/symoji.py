import re

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

def convert_shortcodes_to_emojis(text):
    pattern = re.compile(r'\|:(\w+?):\|')
    return pattern.sub(lambda match: SHORTCODE_TO_UNICODE.get(f'|:{match.group(1)}:|', match.group(0)), text)

# def convert_shortcodes_to_emojis(text):
#     pattern = re.compile(r'(\|\:\w+?\:\|)')
#     return pattern.sub(lambda match: SHORTCODE_TO_UNICODE.get(match.group(1), match.group(1)), text)
