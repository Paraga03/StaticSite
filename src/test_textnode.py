import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_differnent_text(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("World", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_text_type(self):
        node1 = TextNode("Sample text", TextType.TEXT)
        node2 = TextNode("Sample text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_url_vs_none(self):
        node1 = TextNode("Link", TextType.LINK, url="https://example.com")
        node2 = TextNode("Link", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_eq_all_fields(self):
        node1 = TextNode("Image", TextType.IMAGE, url="https://img.com")
        node2 = TextNode("Image", TextType.IMAGE, url="https://img.com")
        self.assertEqual(node1,node2)

if __name__ == "__main__":
    unittest.main()
