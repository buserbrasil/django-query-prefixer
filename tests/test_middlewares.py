from unittest import mock

from django_query_prefixer.middlewares import request_route


def test_request_route_middleware():
    response = object()
    get_response = mock.MagicMock(return_value=response)
    middleware = request_route(get_response=get_response)

    request = mock.MagicMock()
    request.resolver_match.route.route = "/hello"
    request.resolver_match.route.view_name = "hello_world"

    with mock.patch("django_query_prefixer.middlewares.sql_prefixes") as mock_sql_prefixes:
        assert middleware(request) == response

    mock_sql_prefixes.assert_called_with(
        view_name="hello_world",
        route="/hello",
    )

    get_response.assert_called_once_with(request)
