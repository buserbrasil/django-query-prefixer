# django-query-prefixer

The Django Query Prefixer allows you to prepend annotations to every query
executed within your Django project. This can be useful for monitoring. By
adding custom prefixes to queries, you can gain insights into their origin,
and can track their performance in a more organized manner.

## Installation

You can install `django-query-prefixer` using pip:

```shell
pip install django-query-prefixer
```

## Usage

1. Change database engine in your `settings.py` to
`django_query_prefixer.backends.<database backend>`.

```python
DATABASES = {
    "default": {
        "ENGINE": "django_query_prefixer.backends.postgresql",
        "HOST": "127.0.0.1",
        "NAME": "postgres",
        "PASSWORD": "postgres",
        "USER": "postgres",
    }
}
```

2. (Optional) Add `django_query_prefixer.middlewares.request_route` to the
`MIDDLEWARE` list. This middleware adds `route` and `view_name` prefixes to
SQL queries.

```python
MIDDLEWARE = [
    "django_query_prefixer.middlewares.request_route",
    # ... 
]
```

3. Now, whenever queries are executed in your Django project, the configured prefixes
will be automatically added to those queries. For example, a query like this:

```python
User.objects.filter(username='bob')
```

will be executed as:

```sql
/* view_name=example route=/example */ SELECT ... FROM "auth_user" WHERE ("auth_user"."username" = 'bob')
```

You can add additional context to queries using the `sql_prefixes` _contextmanager_:

```python
from django_query_prefixer import sql_prefixes 

with sql_prefixes(user_id=request.user.id, foo="bar"):
    User.objects.filter(username='bob')
````

```sql
/* user_id=X foo=bar view_name=example route=/example */ SELECT ... FROM "auth_user" WHERE ("auth_user"."username" = 'bob')
```

## Contributing

Contributions to `django-query-prefixer` are welcome! If you find a bug, want to
add a new feature, or improve the documentation, please open an issue or submit
a pull request in the GitHub repository.
