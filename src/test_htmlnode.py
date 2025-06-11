import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_multiple_attributes(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_with_single_attribute(self):
        node = HTMLNode(tag="img", props={"src": "image.png"})
        expected = ' src="image.png"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_with_no_attributes(self):
        node = HTMLNode(tag="p")
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_order_independent(self):
        node = HTMLNode(tag="a", props={"target": "_blank", "href": "https://example.com"})
        result = node.props_to_html()
        self.assertIn('href="https://example.com"', result)
        self.assertIn('target="_blank"', result)


if __name__ == "__main__":
    unittest.main()

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("p", "Second paragraph")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            "<div><p>First paragraph</p><p>Second paragraph</p></div>"
        )

    def test_to_html_with_props(self):
        child = LeafNode("p", "Text")
        parent = ParentNode("div", [child], props={"class": "container"})
        self.assertEqual(
            parent.to_html(),
            '<div class="container"><p>Text</p></div>'
        )

    def test_missing_tag_raises_error(self):
        child = LeafNode("p", "Text")
        with self.assertRaises(ValueError):
            ParentNode(None, [child])

    def test_empty_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_deeply_nested_structure(self):
        node = ParentNode("div", [
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "Item 1")]),
                ParentNode("li", [LeafNode(None, "Item 2")]),
            ])
        ])
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        )

if __name__ == "__main__":
    unittest.main()

