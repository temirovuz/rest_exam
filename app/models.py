from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

APP_TYPE = (
    ('website', 'website'),
    ('mobile', 'mobile'),
    ('desktop', 'desktop'),
)


# User Password Manager
class UserPasswordManager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    application_type = models.CharField(choices=APP_TYPE, max_length=20, default='website')
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
