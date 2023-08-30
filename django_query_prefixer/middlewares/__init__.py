from django.urls import resolve
from django_query_prefixer import sql_prefixes


def request_route(get_response):
    def middleware(request):
        if request.resolver_match is not None:
            route = request.resolver_match.route
        else:
            route = resolve(request.path_info)

        with sql_prefixes(
            view_name=route.view_name,
            route=escape_comment_markers(route.route),
        ):
            return get_response(request)

    return middleware


def escape_comment_markers(value):
    return value.replace("/*", r"\/\*").replace("*/", r"\*\/")
