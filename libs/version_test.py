import unittest

from libs.version import BinaryVersion, parse_version


class TestParseVersion(unittest.TestCase):
    def test_parse_tag(self) -> None:
        self.assertEqual(parse_version("0.1"), BinaryVersion(release_tag="0.1"))

    def test_parse_tag_distance(self) -> None:
        self.assertEqual(
            parse_version("0.1.dev100+gbd1cf58"),
            BinaryVersion(next_version="0.1", dev_distance="100", revision_hash="bd1cf58"),
        )

    def test_parse_tag_dirty(self) -> None:
        self.assertEqual(
            parse_version("0.1+d20240403"),
            BinaryVersion(release_tag="0.1", dirty_workdir="20240403"),
        )

    def test_parse_tag_distance_dirty(self) -> None:
        self.assertEqual(
            parse_version("0.1.dev100+gbd1cf58.d20240403"),
            BinaryVersion(
                next_version="0.1",
                dev_distance="100",
                revision_hash="bd1cf58",
                dirty_workdir="20240403",
            ),
        )
