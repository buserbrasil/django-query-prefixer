from unittest import mock

from django_query_prefixer.middlewares import request_route


def test_request_route_middleware():
    response = object()
    get_response = mock.MagicMock(return_value=response)
    middleware = request_route(get_response=get_response)

    request = mock.MagicMock()
    request.resolver_match.route = "/hello"

    def hello_world():
        pass

    with mock.patch("django_query_prefixer.middlewares.set_prefix") as mock_set_prefix, mock.patch(
        "django_query_prefixer.middlewares.remove_prefix"
    ) as mock_remove_prefix:
        middleware.process_view(request, hello_world, [], {})
        assert middleware(request) == response

        mock_set_prefix.assert_has_calls(
            [
                mock.call(key="view_name", value=f"test_middlewares.hello_world"),
                mock.call(key="route", value=f"/hello"),
            ]
        )
        mock_remove_prefix.assert_has_calls(
            [
                mock.call("view_name"),
                mock.call("route"),
            ],
        )
