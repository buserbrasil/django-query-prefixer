import pytest
from django_query_prefixer import _prefixes


@pytest.fixture(autouse=True)
def reset_context():
    yield
    _prefixes.set({})
