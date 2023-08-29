from django.contrib.gis.db.backends.postgis.base import DatabaseWrapper as BaseDatabaseWrapper

from ...cursor import CursorWrapper


class DatabaseWrapper(BaseDatabaseWrapper):
    def create_cursor(self, name=None):
        cursor = super().create_cursor(name)
        return CursorWrapper(cursor)
