# temp_cache
Simply python3 library for creating temporary cache file library.
We can create cache file on `/tmp/` dir only wrapping `str`/`Path` with `TempCache`. 

## Install
```bash
pip install git+https://github.com/Hiroshiba/temp_cache
```

## Usage
The cache file will create when `open` builtin function is called.

```python
from temp_cache import TempCache

cache = TempCache('/path/to/source')

# copy file to cache path `/tmp/path/to/source` and read from cache file.
with open(cache) as f:
    f.read()
```

If anyone need file path as `str`, you can create cache file with calling `str` builtin function.

```python
# for example, numpy.load need string file path.
import numpy

cache = TempCache('/path/to/source.npy')

# when __str__ method is called, `TempCache` create cache file and return cache path.
numpy.load(str(cache))
```

With calling `create_cache` method, you can explicit create cache file.
```python
cache.create_cache()
with open(cache.dst_path) as f:
    f.read()
```

## LICENSE
MIT LICENSE
