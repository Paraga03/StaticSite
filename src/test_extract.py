import unittest
from extract import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    
    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "![img1](https://img1.png) and ![img2](https://img2.jpg)"
        )
        self.assertListEqual([
            ("img1", "https://img1.png"),
            ("img2", "https://img2.jpg"),
        ], matches)

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images("No images here!")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_single(self):
        matches = extract_markdown_links(
            "Check this [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "Go to [Google](https://google.com) or [Bing](https://bing.com)"
        )
        self.assertListEqual([
            ("Google", "https://google.com"),
            ("Bing", "https://bing.com")
        ], matches)

    def test_extract_markdown_links_none(self):
        matches = extract_markdown_links("Nothing to link here.")
        self.assertListEqual([], matches)

    def test_ignore_image_as_link(self):
        matches = extract_markdown_links("This is an image: ![alt](https://img.com)")
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()

