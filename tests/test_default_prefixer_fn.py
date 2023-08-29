from django_query_prefixer import default_prefixer_fn, set_prefix


def test_default_prefixer_fn():
    set_prefix("test1", "value1")
    set_prefix("test2", "value2")

    assert default_prefixer_fn() == "test1=value1 test2=value2"
