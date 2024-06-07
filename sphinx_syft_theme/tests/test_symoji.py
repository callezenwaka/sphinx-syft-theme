import unittest
from symoji.symoji import unicode_to_shortcode, shortcode_to_unicode, convert_shortcodes_to_emojis

class TestEmojiConverter(unittest.TestCase):

    def test_unicode_to_shortcode(self):
        self.assertEqual(unicode_to_shortcode("\U0001F468\u200D\U0001F4BB"), ":man_technologist:")
        self.assertEqual(unicode_to_shortcode("\U0001F468\U0001F3FF\u200D\U0001F4BB"), ":man_technologist_dark_skin_tone:")
        self.assertIsNone(unicode_to_shortcode("👨‍🚀"))  # Example of a non-existent mapping

    def test_shortcode_to_unicode(self):
        self.assertEqual(shortcode_to_unicode(":man_technologist:"), "\U0001F468\u200D\U0001F4BB")
        self.assertEqual(shortcode_to_unicode(":man_technologist_dark_skin_tone:"), "\U0001F468\U0001F3FF\u200D\U0001F4BB")
        self.assertIsNone(shortcode_to_unicode(":astronaut:"))  # Example of a non-existent mapping

    def test_convert_shortcodes_to_emojis(self):
        text = "This text includes a man technologist |:man_technologist_dark_skin_tone:| and a woman technologist too! |:woman_technologist:|"
        expected = "This text includes a man technologist |👨🏿‍💻| and a woman technologist too! |👩‍💻|"
        self.assertEqual(convert_shortcodes_to_emojis(text), expected)

if __name__ == '__main__':
    unittest.main()
