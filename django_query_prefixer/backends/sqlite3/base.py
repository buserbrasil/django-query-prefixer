from django.db.backends.sqlite3.base import DatabaseWrapper as BaseDatabaseWrapper

from ...cursor import CursorWrapper


class DatabaseWrapper(BaseDatabaseWrapper):
    def create_cursor(self, name=None):
        cursor = super().create_cursor(name)
        return CursorWrapper(cursor)
