# Garpix User

Auth module for Django/DRF projects. Part of GarpixCMS.

Used packages: 

* [django rest framework](https://www.django-rest-framework.org/api-guide/authentication/)
* [social-auth-app-django](https://github.com/python-social-auth/social-app-django)
* [django-rest-framework-social-oauth2](https://github.com/RealmTeam/django-rest-framework-social-oauth2)
* etc; see setup.py

## Quickstart

Install with pip:

```bash
pip install garpix_user
```

Add the `garpix_user` to your `INSTALLED_APPS`:

```python
# settings.py

# ...
INSTALLED_APPS = [
    # ...
    'garpix_user',
]
```

and to migration modules:

```python
# settings.py

# ...
MIGRATION_MODULES = {
    'garpix_user': 'app.migrations.garpix_user',
}
```

Add to `urls.py`:

```python
from garpix_user.views import LogoutView, LoginView

# ...
urlpatterns = [
    # ...
    # garpix_user
    path('', include(('garpix_user.urls', 'user'), namespace='garpix_user')),

]
```

For custom auth with phone and email use this in `settings.py`:

```python
# ...

AUTHENTICATION_BACKENDS = (
    # Django
    'garpix_user.utils.backends.CustomAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

```

and `USERNAME_FIELDS` to your `User` model:

```python
# user.models.user.py

from garpix_user.mixins.models import GarpixUserMixin


class User(GarpixUserMixin):
    
    USERNAME_FIELDS = ('email',)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


```

## With Django Rest Framework

Import settings from `garpix_user`:

```python
# settings.py
from garpix_user.settings import *

```

Add this for SPA:

```python
# ...
INSTALLED_APPS += [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    # ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': {
        'garpix_auth.rest.authentication.MainAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    }
}

```

## Email and phone confirmation, password restoring

To use email and phone confirmation or (and) restore password functionality add the `garpix_notify` to your `INSTALLED_APPS`:

```python
# settings.py

# ...
INSTALLED_APPS = [
    # ...
    'garpix_notify',
]
```
and to migration modules:

```python
# settings.py

MIGRATION_MODULES = {
    'garpix_notify': 'app.migrations.garpix_notify',
}
```

Add corresponding settings:

```python

# settings.py

GARPIX_USER = {
    'USE_EMAIL_CONFIRMATION': True,
    'USE_PHONE_CONFIRMATION': True,
    'USE_EMAIL_RESTORE_PASSWORD': True,
    'USE_PHONE_RESTORE_PASSWORD': True,
}

# Hint: see all available settings in the end of this document.

```

You also need to add notify events:

```python
# settings.py

NOTIFY_EVENTS.update(GARPIX_USER_NOTIFY_EVENTS)

```

You can specify email and phone code length and lifetime:
```python
GARPIX_CONFIRM_CODE_LENGTH = 6
GARPIX_CONFIRM_PHONE_CODE_LIFE_TIME = 5  # in minutes
GARPIX_CONFIRM_EMAIL_CODE_LIFE_TIME = 2  # in days
```

If you need to use pre-registration email or phone confirmation, you need to set corresponding variables to True:
```python

# settings.py

GARPIX_USER = {
    'USE_PREREGISTRATION_EMAIL_CONFIRMATION': True,
    'USE_PREREGISTRATION_PHONE_CONFIRMATION': True,
}

# Hint: see all available settings in the end of this document.

```

If you need to use email confirmation by link, you need to set corresponding variable:
```python

# settings.py

GARPIX_USER = {
    'USE_EMAIL_LINK_CONFIRMATION': True,
    'EMAIL_CONFIRMATION_LINK_REDIRECT': '',  # link to the page user needs to see after email confirmation
}

# Hint: see all available settings in the end of this document.

```

## Referral links

You can also use referral links in your project with garpix_user. To add this functionality, just add the corresponding settings:

```python  

# settings.py

GARPIX_USER = {
    'USE_REFERRAL_LINKS': True,
    'REFERRAL_REDIRECT_URL': '/', # link to the page user needs to see
}

```

## UserSession

Using `garpix_user` you can also store info about unregistered user sessions. The package already consists of model and views for it.

To create the unregistered user send `POST` request to `{API_URL}/user_session/create_user_session/`

The request returns `UserSession` object with `token_number` field. You need to send this token number in each request passing in to header as `user-session-token`.


## All available settings

```python
    
# settings.py

GARPIX_USER = {
    # base settings
    'USE_REFERRAL_LINKS': False,
    'REFERRAL_REDIRECT_URL': '/',
    # email/phone confirmation
    'USE_EMAIL_CONFIRMATION': True,
    'USE_PHONE_CONFIRMATION': True,
    'USE_PREREGISTRATION_EMAIL_CONFIRMATION': True,
    'USE_PREREGISTRATION_PHONE_CONFIRMATION': True,
    'USE_EMAIL_LINK_CONFIRMATION': True,
    'EMAIL_CONFIRMATION_LINK_REDIRECT': '',
    'CONFIRM_CODE_LENGTH': 6,
    'TIME_LAST_REQUEST': 1,
    'CONFIRM_PHONE_CODE_LIFE_TIME': 5,  # in minutes
    'CONFIRM_EMAIL_CODE_LIFE_TIME': 2,  # in days
    # restore password
    'USE_EMAIL_RESTORE_PASSWORD': True,
    'USE_PHONE_RESTORE_PASSWORD': True,
    # response messages
    'WAIT_RESPONSE': 'Не прошло 1 мин с момента предыдущего запроса',
    'USER_REGISTERED_RESPONSE': 'Пользователь с таким {field} уже зарегистрирован',  # as 'field' will be used email/phone according to the request
    'INCORRECT_CODE_RESPONSE': 'Некорретный код',
    'NO_TIME_LEFT_RESPONSE': 'Код недействителен. Запросите повторно',
    'NOT_AUTHENTICATED_RESPONSE': 'Учетные данные не были предоставлены'
}

```

See `garpix_user/tests/test_api.py` for examples.

# Changelog

See [CHANGELOG.md](backend/garpix_user/CHANGELOG.md).

# Contributing

See [CONTRIBUTING.md](backend/garpix_user/CONTRIBUTING.md).

# License

[MIT](LICENSE)

---

Developed by Garpix / [https://garpix.com](https://garpix.com)