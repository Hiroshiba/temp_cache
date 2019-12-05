import filecmp
from os import rename, PathLike
from pathlib import Path
from tempfile import NamedTemporaryFile

from typing import Union


class TempCache(PathLike):
    r"""

    """
    def __init__(self, src_path: Union[str, Path], dst_path: Path = None, cache_dir: Path = Path('/tmp/')):
        src_path = Path(src_path)
        if dst_path is None:
            dst_path = cache_dir.joinpath(*src_path.absolute().parts[1:])

        self.src_path = src_path
        self.dst_path = dst_path

    def create_cache(self):
        if self.dst_path.exists() and filecmp.cmp(self.src_path, self.dst_path):
            self.dst_path.touch()
            return

        self.dst_path.parent.mkdir(parents=True, exist_ok=True)

        with NamedTemporaryFile(dir=str(self.dst_path.parent), delete=False) as f:
            f.write(self.src_path.read_bytes())

        rename(f.name, str(self.dst_path))

    def __str__(self):
        self.create_cache()
        return str(self.dst_path)

    def __fspath__(self):
        return str(self)
