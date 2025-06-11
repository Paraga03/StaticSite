import unittest
from markdown_to_html import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        md = "# My Blog Title"
        self.assertEqual(extract_title(md), "My Blog Title")

    def test_title_with_extra_spaces(self):
        md = "  #   Spaced Title   "
        self.assertEqual(extract_title(md), "Spaced Title")

    def test_multiple_lines(self):
        md = "Some text\n# Real Title\nMore text"
        self.assertEqual(extract_title(md), "Real Title")

    def test_no_title(self):
        md = "## Subtitle\n### Another Header"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_title_not_first_line(self):
        md = "\n\n# After blank lines"
        self.assertEqual(extract_title(md), "After blank lines")

if __name__ == "__main__":
    unittest.main()

