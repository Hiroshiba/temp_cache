from pathlib import Path

import pytest

from temp_cache.temp_cache import TempCache


@pytest.fixture
def src_path():
    return Path(__file__)


def _remove_cache(cache: TempCache):
    if cache.dst_path.exists():
        cache.dst_path.unlink()
    assert not cache.dst_path.exists()


def test_temp_cache_will_create_at_tmp_dir(src_path: Path):
    cache = TempCache(src_path)
    cache.create_cache()
    assert str(cache.dst_path) == str(Path('/tmp/') / '/'.join(src_path.parts[1:]))


def test_create_cache(src_path: Path):
    cache = TempCache(src_path)
    _remove_cache(cache)

    cache.create_cache()
    assert cache.dst_path.exists()


def test_create_cache_with_open(src_path: Path):
    cache = TempCache(src_path)
    _remove_cache(cache)

    with open(cache):
        pass
    assert cache.dst_path.exists()


def test_create_cache_path_with_str(src_path: Path):
    cache = TempCache(src_path)
    _remove_cache(cache)

    _ = str(cache)
    assert cache.dst_path.exists()


def test_recreate_cache(src_path: Path):
    cache = TempCache(src_path)
    _remove_cache(cache)

    cache.create_cache()
    assert cache.dst_path.exists()

    _remove_cache(cache)

    cache.create_cache()
    assert cache.dst_path.exists()


def test_recreate_cache_when_file_is_different(src_path: Path):
    cache = TempCache(src_path)
    _remove_cache(cache)

    cache.create_cache()
    text = cache.dst_path.read_text()

    cache.dst_path.write_text('other text')
    assert cache.dst_path.read_text() != text

    cache.create_cache()
    assert cache.dst_path.read_text() == text
