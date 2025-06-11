import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_heading(self):
        markdown = "# This is a heading"
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, ["# This is a heading"])

    def test_multiple_blocks(self):
        markdown = "# Heading\n\nThis is a paragraph.\n\n- Item 1\n- Item 2"
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [
            "# Heading",
            "This is a paragraph.",
            "- Item 1\n- Item 2"
        ])

    def test_trailing_whitespace(self):
        markdown = "  # Heading  \n\n   Paragraph with spaces   \n\n\n"
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [
            "# Heading",
            "Paragraph with spaces"
        ])

    def test_empty_string(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_extra_newlines_between_blocks(self):
        markdown = "# Heading\n\n\n\nParagraph\n\n\n- List item"
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, [
            "# Heading",
            "Paragraph",
            "- List item"
        ])



class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote\n> And another line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_block(self):
        block = "- Item one\n- Item two\n- Item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        block = "This is a paragraph of regular text.\nIt goes over two lines."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_block_should_be_paragraph(self):
        block = "- Item 1\n2. Not valid ordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()


