from django.urls import resolve
from django_query_prefixer import set_prefix


def request_route(get_response):
    def middleware(request):
        if request.resolver_match is not None:
            route = request.resolver_match.route
        else:
            route = resolve(request.path_info)

        set_prefix("view_name", route.view_name)
        set_prefix("route", escape_comment_markers(route.route))

        response = get_response(request)
        return response

    return middleware


def escape_comment_markers(value):
    return value.replace("/*", r"\/\*").replace("*/", r"\*\/")
