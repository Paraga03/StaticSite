import unittest
from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter, split_nodes_images, split_nodes_links

class TestSplitNodes(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is `code` example", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" example", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_bold(self):
        node = TextNode("This is **bold** and **strong**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("strong", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_unbalanced_delimiters(self):
        node = TextNode("This is `broken code", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])  

    def test_non_text_type_node(self):
        node = TextNode("Just a link", TextType.LINK, "https://example.com")
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])  

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [])  

    
    def test_split_nodes_image_single(self):
        input_nodes = [
            TextNode(
                "Here is an image: ![alt text](https://example.com/image.png)",
                TextType.TEXT,
            )
        ]
        expected = [
            TextNode("Here is an image: ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
        ]
        result = split_nodes_images(input_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple(self):
        input_nodes = [
            TextNode(
                "![alt1](url1) and then ![alt2](url2)", TextType.TEXT
            )
        ]
        expected = [
            TextNode("alt1", TextType.IMAGE, "url1"),
            TextNode(" and then ", TextType.TEXT),
            TextNode("alt2", TextType.IMAGE, "url2"),
        ]
        result = split_nodes_images(input_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_link_single(self):
        input_nodes = [
            TextNode(
                "Here is a [link](https://example.com)", TextType.TEXT
            )
        ]
        expected = [
            TextNode("Here is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]
        result = split_nodes_links(input_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_link_multiple(self):
        input_nodes = [
            TextNode(
                "[first](url1) and [second](url2)", TextType.TEXT
            )
        ]
        expected = [
            TextNode("first", TextType.LINK, "url1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.LINK, "url2"),
        ]
        result = split_nodes_links(input_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_non_text(self):
        input_nodes = [TextNode("Bold text", TextType.BOLD)]
        result_image = split_nodes_images(input_nodes)
        result_link = split_nodes_links(input_nodes)
        self.assertEqual(result_image, input_nodes)
        self.assertEqual(result_link, input_nodes)

if __name__ == "__main__":
    unittest.main()

