from enum import Enum

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")

    blocks = [block.strip() for block in raw_blocks if block.strip() !=""]

    return blocks

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(block):
    lines = block.splitlines()

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if lines[0].startswith("#"):
        if 1 <= len(lines[0].split(" ")[0]) <= 6 and lines[0].startswith("#" * len(lines[0].split(" ")[0]) + " "):
            return BlockType.HEADING

    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    try:
        for i, line in enumerate(lines):
            expected_prefix = f"{i + 1}. "
            if not line.strip().startswith(expected_prefix):
                break
        else:
            return BlockType.ORDERED_LIST
    except:
        pass

    return BlockType.PARAGRAPH

