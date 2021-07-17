from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    '''Manager to user profiles'''
    
    ''''Create common user'''
    def create_user(self, email, name, password=None):
        """Create new user profle"""
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        '''Set the password taking care about the hash'''
        user.set_password(password)

        '''Save the user in our database'''
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)


class Userprofile(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Get full name'''
        return self.name
    
    def get_short_name(self):
        '''Get Short name'''
        return self.name

    def __str__(self):
        '''Return User as string representation'''
        return self.email

    
'''After all of this, we need to add our Authentification
user model in settings.py, at the end add the next line:
AUTH_USER_MODEL = "<appname>.<modelname>" '''

