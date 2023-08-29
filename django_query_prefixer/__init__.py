from contextvars import ContextVar

__version__ = "0.1.0"


def set_prefix(key: str, value: str):
    prefixes = _prefixes.get({})
    prefixes[key] = value
    _prefixes.set(prefixes)


def get_prefixes() -> dict[str, str]:
    return _prefixes.get({})


def default_prefixer_fn() -> str:
    prefixes = get_prefixes()
    return " ".join(f"{key}={value}" for key, value in prefixes.items())


_prefixes: ContextVar[dict[str, str]] = ContextVar("sql_prefixes")
