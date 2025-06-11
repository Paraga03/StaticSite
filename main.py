import os
import shutil

from copy_static import copy_static_files
from src.textnode import TextNode, TextType
from site_generator import generate_page, generate_pages_recursive


def main():

    if os.path.exists("public"):
        shutil.rmtree("public")


    copy_static_files("static", "public")


    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()

