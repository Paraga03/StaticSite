import os
import shutil
import sys
from copy_static import copy_static_files
from src.textnode import TextNode, TextType
from site_generator import generate_page, generate_pages_recursive


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    output_dir = "docs"

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)


    copy_static_files("static", output_dir)


    generate_pages_recursive("content", "template.html", output_dir, basepath)

if __name__ == "__main__":
    main()

