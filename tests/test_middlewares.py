from unittest import mock

from django_query_prefixer.middlewares import request_route


def test_request_route_middleware():
    response = object()
    get_response = mock.MagicMock(return_value=response)
    middleware = request_route(get_response=get_response)

    request = mock.MagicMock()
    request.resolver_match.route.route = "/hello"
    def hello_world():
        pass

    with mock.patch("django_query_prefixer.middlewares.set_prefix") as mock_set_prefix, \
            mock.patch("django_query_prefixer.middlewares.remove_prefix") as mock_remove_prefix:
        middleware.process_view(request, hello_world, [], {})
        assert middleware(request) == response

    assert mock_set_prefix.call_args_list[0].kwargs == {"key": "view_name", "value": f"{hello_world.__module__}.hello_world"}
    assert mock_set_prefix.call_args_list[1].kwargs == {"key": "route", "value": "/hello"}
    assert mock_remove_prefix.call_args_list[0].args[0] == "view_name"
    assert mock_remove_prefix.call_args_list[1].args[0] == "route"
