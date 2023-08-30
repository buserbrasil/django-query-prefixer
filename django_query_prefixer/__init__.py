from contextlib import contextmanager
from typing import Dict
from contextvars import ContextVar

__version__ = "0.1.0"


@contextmanager
def sql_prefixes(**kwargs):
    for key, value in kwargs.items():
        if not isinstance(value, str):
            value = repr(value)
        set_prefix(key, value)

    yield

    for key in kwargs.keys():
        remove_prefix(key)


def set_prefix(key: str, value: str):
    prefixes = _prefixes.get({})
    prefixes[key] = value
    _prefixes.set(prefixes)


def get_prefixes() -> Dict[str, str]:
    return _prefixes.get({})


def remove_prefix(key: str):
    prefixes = _prefixes.get({})
    prefixes.pop(key, None)
    _prefixes.set(prefixes)


def default_prefixer_fn() -> str:
    prefixes = get_prefixes()
    return " ".join(f"{key}={value}" for key, value in prefixes.items())


_prefixes: ContextVar[Dict[str, str]] = ContextVar("sql_prefixes")
