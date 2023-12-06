from django.urls import resolve
from django_query_prefixer import set_prefix, remove_prefix


class RequestRouteMiddleware:
    def  __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        response = request.get_response(request)
        remove_prefix("view_name")
        remove_prefix("route")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        set_prefix(key="view_name", value=f"{view_func.__module__}.{view_func.__name__}")
        set_prefix(
            key="route",
            value=escape_comment_markers(request.resolver_match.route.route)
        )
        return view_func


def request_route(get_response):
    return RequestRouteMiddleware(get_response)


def escape_comment_markers(value):
    return value.replace("/*", r"\/\*").replace("*/", r"\*\/")
