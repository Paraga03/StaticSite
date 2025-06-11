import os
from src.markdown_to_html import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()


    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()


    try:
        title = extract_title(markdown_content)
    except Exception as e:
        raise Exception(f"Error extracting title from {from_path}: {e}")


    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()


    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)


    os.makedirs(os.path.dirname(dest_path), exist_ok=True)


    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)

                rel_path = os.path.relpath(from_path, dir_path_content)
                rel_path_html = rel_path[:-3] + ".html"
                dest_path = os.path.join(dest_dir_path, rel_path_html)

                print(f"Generating page from {from_path} to {dest_path} using {template_path}")
                generate_page(from_path, template_path, dest_path)

