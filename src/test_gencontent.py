import unittest

from gencontent import *

class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is the title
## This is a subtitle
This is a paragraph
        """
        title = extract_title(md)
        self.assertEqual(title, "This is the title")

    def test_extract_title_no_title(self):
        md = """
This is a paragraph without a title
        """
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()