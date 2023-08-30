from django_query_prefixer import get_prefixes, set_prefix, sql_prefixes


def test_sql_prefixes_context_manager():
    with sql_prefixes(test="dummy", n=42):
        assert get_prefixes() == {"test": "dummy", "n": "42"}
    assert get_prefixes() == {}


def test_set_prefixes():
    set_prefix("key1", "value1")

    assert get_prefixes() == {"key1": "value1"}


def test_set_prefixes_override_previous_value():
    set_prefix("key1", "value1")
    set_prefix("key1", "value2")

    assert get_prefixes() == {"key1": "value2"}


def test_set_prefixes_multiple():
    set_prefix("key1", "value1")
    set_prefix("key2", "value2")

    assert get_prefixes() == {
        "key1": "value1",
        "key2": "value2",
    }
