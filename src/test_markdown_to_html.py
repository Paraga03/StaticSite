import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHtml(unittest.TestCase):
    def test_single_heading(self):
        md = "# This is a heading"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1></div>")

    def test_paragraph(self):
        md = "This is a simple paragraph."
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><p>This is a simple paragraph.</p></div>")

    def test_code_block(self):
        md = "```\ncode block\nmultiple lines\n```"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><pre><code>code block\nmultiple lines</code></pre></div>")

    def test_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>")

    def test_ordered_list(self):
        md = "1. First\n2. Second\n3. Third"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>")

    def test_quote_block(self):
        md = "> This is a quote\n> spanning two lines"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><blockquote>This is a quote\nspanning two lines</blockquote></div>")

    def test_mixed_blocks(self):
        md = "# Heading\n\nParagraph text\n\n- Item A\n- Item B"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h1>Heading</h1><p>Paragraph text</p><ul><li>Item A</li><li>Item B</li></ul></div>")

if __name__ == "__main__":
    unittest.main()

