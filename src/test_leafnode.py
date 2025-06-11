import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        node = LeafNode("p", "Hello, world!", {"class": "intro"})
        expected = '<p class="intro">Hello, world!</p>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_without_tag(self):
        node = LeafNode(None, "Just plain text")
        expected = "Just plain text"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_raises_with_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("span", None)

    def test_to_html_with_tag_no_props(self):
        node = LeafNode("em", "Important")
        expected = "<em>Important</em>"
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()

