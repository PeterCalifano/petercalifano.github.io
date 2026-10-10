"""Check the content editing workflow in disposable copies of the website."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(ROOT / "build.py", self.root / "build.py")
        shutil.copytree(ROOT / "content", self.root / "content")

    def build(self):
        return subprocess.run(
            [sys.executable, str(self.root / "build.py")],
            cwd=self.root, capture_output=True, text=True,
        )

    def test_generated_pages_match_sources(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        for page in ROOT.glob("*.html"):
            with self.subTest(page=page.name):
                self.assertEqual(page.read_bytes(), (self.root / page.name).read_bytes())

    def test_edit_paragraphs_bullets_and_italics(self):
        home = self.root / "content/home.md"
        text = home.read_text().replace(
            "## About\n", "## About\n\nA user's café & <test>.\nWrapped line.\n\n"
        )
        home.write_text(text)
        research = self.root / "content/research.md"
        research.write_text(research.read_text().replace(
            "## Perception\n", "## Perception\n\n- A new & editable bullet\n  continued here.\n"
        ))
        beyond = self.root / "content/beyond.md"
        beyond.write_text(beyond.read_text().replace(
            "Regular running and time outdoors.", "Reading *a title* & writing <notes>."
        ))
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "<p>A user's café &amp; &lt;test&gt;. Wrapped line.</p><p>",
            (self.root / "index.html").read_text(),
        )
        self.assertIn(
            "<li>A new &amp; editable bullet continued here.</li>",
            (self.root / "research.html").read_text(),
        )
        self.assertIn(
            "Reading <em>a title</em> &amp; writing &lt;notes&gt;.",
            (self.root / "beyond.html").read_text(),
        )

    def test_duplicate_section_names_fail(self):
        path = self.root / "content/home.md"
        path.write_text(path.read_text() + "\n## About\n\nDuplicate.\n")
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate section 'About'", result.stderr)

    def test_editing_comments_never_reach_pages(self):
        path = self.root / "content/home.md"
        path.write_text("<!-- Hidden file note. -->\n" + path.read_text().replace(
            "## About\n", "## About\n<!-- Hidden multiline note.\n## Not a section\n-->\n"
        ))
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (ROOT / "index.html").read_bytes(),
            (self.root / "index.html").read_bytes(),
        )

    def test_unclosed_comment_fails(self):
        path = self.root / "content/home.md"
        path.write_text(path.read_text() + "\n<!-- Unclosed note")
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unclosed <!-- editing comment", result.stderr)

    def test_missing_section_names_fail(self):
        path = self.root / "content/research.md"
        path.write_text(path.read_text().replace("## Perception", "## Renamed"))
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("content/research.md: missing section 'Perception'", result.stderr)


if __name__ == "__main__":
    unittest.main()
