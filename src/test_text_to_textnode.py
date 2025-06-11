import unittest
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        text = "Just plain text."
        expected = [TextNode("Just plain text.", TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_bold_text(self):
        text = "Some **bold** word."
        expected = [
            TextNode("Some ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_italic_text(self):
        text = "An _italic_ word."
        expected = [
            TextNode("An ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_code_text(self):
        text = "This has a `code` snippet."
        expected = [
            TextNode("This has a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" snippet.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_link_text(self):
        text = "A [link](https://example.com)"
        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_image_text(self):
        text = "An image ![alt text](https://img.com/pic.png)"
        expected = [
            TextNode("An image ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://img.com/pic.png")
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_combined_markdown(self):
        text = "Hello **bold**, _italic_, `code`, ![img](url) and [link](url)"
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(", ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "url"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url")
        ]
        self.assertEqual(text_to_textnodes(text), expected)

if __name__ == "__main__":
    unittest.main()

