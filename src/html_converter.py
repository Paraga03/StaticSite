from .htmlnode import LeafNode  
from .textnode import TextNode, TextType  


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode object")

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("Link TextNode must have a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Image TextNode must have a URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    else:
        raise Exception(f"Unknown text type: {text_node.text_type}")

