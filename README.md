# Custom-User-Model
Django: Login using Email instead of Password
Case Insensitive Login and Register
NOTE: backends.py should be configured on setting.py
----MUST ADD ON SETTINGS.PY----
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'user.backends.backends.CaseInsensitiveModelBackend'
)
