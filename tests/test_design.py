import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DesignTests(unittest.TestCase):
    def test_curriculum_stays_empty_until_reviewed(self):
        self.assertEqual({'areas': []}, json.loads((ROOT / 'content' / 'spiral.json').read_text(encoding='utf-8')))

    def test_local_document_links_resolve_inside_repository(self):
        files = [ROOT / 'README.md', *sorted((ROOT / 'docs').glob('*.md'))]
        for file in files:
            for target in re.findall(r'\]\(([^)]+)\)', file.read_text(encoding='utf-8')):
                if target.startswith(('https://', '#')):
                    continue
                resolved = (file.parent / target.split('#')[0]).resolve()
                with self.subTest(document=file.name, target=target):
                    self.assertTrue(resolved.is_relative_to(ROOT))
                    self.assertTrue(resolved.is_file())

    def test_handoff_has_required_documents(self):
        for name in ['PRODUCT.md', 'LITERATURE.md', 'EXPERIENCE.md', 'DATA-AND-PRIVACY.md', 'DECISIONS.md', 'ROADMAP.md']:
            self.assertTrue((ROOT / 'docs' / name).is_file())


if __name__ == '__main__':
    unittest.main()
