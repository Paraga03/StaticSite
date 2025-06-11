from .textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            new_nodes.append(node)
            continue

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(r"(!\[[^\]]+\]\([^)]+\))", node.text)
        for part in parts:
            if part == "":
                continue
            match = re.match(r"!\[([^\]]+)\]\(([^)]+)\)", part)
            if match:
                alt_text, url = match.groups()
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(r"(\[[^\]]+\]\([^)]+\))", node.text)
        for part in parts:
            if part == "":
                continue
            match = re.match(r"\[([^\]]+)\]\(([^)]+)\)", part)
            if match:
                anchor_text, url = match.groups()
                new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes

