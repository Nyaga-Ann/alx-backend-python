INSTALLED_APPS = [
    ...,
    'rest_framework',  # DRF
    'chats',           # Your new app
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
