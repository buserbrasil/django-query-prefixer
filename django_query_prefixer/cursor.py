from django.conf import settings
from django.utils.module_loading import import_string


class CursorWrapper:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, sql, params=None):
        prefix = self.generate_prefix()
        sql = f"/* {prefix} */\n{sql}"
        return self.cursor.execute(sql, params)

    def executemany(self, sql, param_list):
        prefix = self.generate_prefix()
        sql = f"/* {prefix} */\n{sql}"
        return self.cursor.executemany(sql, param_list)

    def generate_prefix(self):
        prefixer_fn = getattr(settings, "DJANGO_QUERY_PREFIXER_FUNCTION", "django_query_prefixer.default_prefixer_fn")
        fn = import_string(prefixer_fn)
        return fn()

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
