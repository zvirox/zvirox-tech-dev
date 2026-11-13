import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestLocalPostImages(unittest.TestCase):
    def test_post_images_exist_locally(self):
        missing = []
        for post in (ROOT / "_posts").glob("*.md"):
            content = post.read_text(encoding="utf-8")
            sources = re.findall(r"!\[[^]]*\]\(([^)]+)\)|<img\b[^>]*\bsrc=[\"']([^\"']+)", content)
            for markdown_src, html_src in sources:
                src = markdown_src or html_src
                if src.startswith(("https://", "http://", "data:", "#")):
                    continue
                path = src.split("?", 1)[0].split("#", 1)[0]
                if path.startswith("/"):
                    asset = ROOT / path.lstrip("/")
                else:
                    asset = post.parent / path
                if not asset.is_file():
                    missing.append(f"{post.relative_to(ROOT)}: {src}")
        self.assertEqual(missing, [], "Missing local post images:\n" + "\n".join(missing))


if __name__ == "__main__":
    unittest.main()
