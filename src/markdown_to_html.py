from .block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from .htmlnode import ParentNode, LeafNode
from .textnode import TextNode, TextType
from .html_converter import text_node_to_html_node
from .text_to_textnode import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            heading_level = len(block.split(" ")[0])
            content = block[heading_level + 1:]
            children.append(ParentNode(f"h{heading_level}", text_to_children(content)))

        elif block_type == BlockType.PARAGRAPH:
            children.append(ParentNode("p", text_to_children(block)))

        elif block_type == BlockType.CODE:
            code_content = "\n".join(block.split("\n")[1:-1])
            code_node = LeafNode("code", code_content)
            children.append(ParentNode("pre", [code_node]))

        elif block_type == BlockType.QUOTE:
            lines = [line[2:] if line.startswith("> ") else line[1:] for line in block.split("\n")]
            quote_text = "\n".join(lines)
            children.append(ParentNode("blockquote", text_to_children(quote_text)))

        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            li_nodes = [ParentNode("li", text_to_children(item[2:])) for item in items]
            children.append(ParentNode("ul", li_nodes))

        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            li_nodes = [ParentNode("li", text_to_children(item[item.index(" ") + 1:])) for item in items]
            children.append(ParentNode("ol", li_nodes))

    return ParentNode("div", children)

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    raise ValueError("No H1 (#) title found in markdown.")
