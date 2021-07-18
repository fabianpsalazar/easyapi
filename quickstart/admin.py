from django.contrib import admin
from quickstart import models

# Register your models here.
'''Now our superuser has permissions to manage "UserProfile" model'''
admin.site.register(models.Userprofile)
