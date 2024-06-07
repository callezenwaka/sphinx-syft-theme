UNICODE_TO_SHORTCODE = {
    "\U0001F468\u200D\U0001F4BB": ":man_technologist:",
    "\U0001F468\U0001F3FF\u200D\U0001F4BB": ":man_technologist_dark_skin_tone:",
    "\U0001F468\U0001F3FB\u200D\U0001F4BB": ":man_technologist_light_skin_tone:",
    "\U0001F468\U0001F3FE\u200D\U0001F4BB": ":man_technologist_medium_dark_skin_tone:",
    "\U0001F468\U0001F3FC\u200D\U0001F4BB": ":man_technologist_medium_light_skin_tone:",
    "\U0001F468\U0001F3FD\u200D\U0001F4BB": ":man_technologist_medium_skin_tone:",
    "\U0001F469\u200D\U0001F4BB": ":woman_technologist:",
    "\U0001F469\U0001F3FF\u200D\U0001F4BB": ":woman_technologist_dark_skin_tone:",
    "\U0001F469\U0001F3FB\u200D\U0001F4BB": ":woman_technologist_light_skin_tone:",
    "\U0001F469\U0001F3FE\u200D\U0001F4BB": ":woman_technologist_medium_dark_skin_tone:",
    "\U0001F469\U0001F3FC\u200D\U0001F4BB": ":woman_technologist_medium_light_skin_tone:",
    "\U0001F469\U0001F3FD\u200D\U0001F4BB": ":woman_technologist_medium_skin_tone:"
}

SHORTCODE_TO_UNICODE = {v: k for k, v in UNICODE_TO_SHORTCODE.items()}

def unicode_to_shortcode(unicode_str):
    return UNICODE_TO_SHORTCODE.get(unicode_str, None)

def shortcode_to_unicode(shortcode):
    return SHORTCODE_TO_UNICODE.get(shortcode, None)

def convert_shortcodes_to_emojis(text):
    for shortcode, unicode_emoji in SHORTCODE_TO_UNICODE.items():
        text = text.replace(shortcode, unicode_emoji)
    return text
