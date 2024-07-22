import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class BinaryVersion(object):
    release_tag: str | None = None
    next_version: str | None = None
    dev_distance: str | None = None
    revision_hash: str | None = None
    dirty_workdir: str | None = None

    def is_dirty(self) -> bool:
        return self.dirty_workdir is not None


def _binsplit(s: str, on: str) -> tuple[str, str]:
    """Convenience function that splits on last occurence of `on` token.

    This allows easily composing multiple splits.
    """
    idx = s.rfind(on)  # we use rfind to tolerate semver version tags, which have multiple '.'
    if idx == -1:
        return s, ""
    return s[:idx], s[idx + len(on) :]


def parse_version(version: str) -> BinaryVersion:
    """Parse setuptools-scm default versioning scheme.

    https://setuptools-scm.readthedocs.io/en/latest/usage/#default-versioning-scheme
    """

    tag_part, rev_part = _binsplit(version, "+")
    tag_or_next_ver, dev_distance = _binsplit(tag_part, ".dev")
    rev, dirty = _binsplit(rev_part, ".d")
    if rev.startswith("d"):
        rev, dirty = "", rev
    rev = rev.removeprefix("g")  # g for git
    rev = rev.removesuffix(".")  # from dirty_time
    dirty = dirty.removeprefix("d")

    tag: str | None
    tag, next_ver = (tag_or_next_ver, None)
    if dev_distance:
        tag, next_ver = None, tag

    return BinaryVersion(
        release_tag=tag,
        next_version=next_ver,
        dev_distance=dev_distance or None,
        revision_hash=rev or None,
        dirty_workdir=dirty or None,
    )


_current_version: BinaryVersion | None = None


def version() -> BinaryVersion:
    global _current_version
    if not _current_version:
        try:
            from libs._version import vcs_version  # type: ignore

            _current_version = parse_version(vcs_version)
        except Exception as e:
            logger.warning(str(e), exc_info=True)
            _current_version = BinaryVersion(dirty_workdir="unknown")

    return _current_version


if __name__ == "__main__":
    import os

    print(f"PEX={os.environ.get('PEX', '')}")
    print(version())
