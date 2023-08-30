from unittest import mock
from django_query_prefixer import get_prefixes
from django_query_prefixer.middlewares import request_route


def test_request_route_middleware():
    response = object()
    get_response = mock.MagicMock(return_value=response)
    middleware = request_route(get_response=get_response)

    request = mock.MagicMock()
    request.resolver_match.route.route = "/hello"
    request.resolver_match.route.view_name = "hello_world"

    assert middleware(request) == response
    assert get_prefixes() == {
        "route": "/hello",
        "view_name": "hello_world",
    }

    get_response.assert_called_once_with(request)
