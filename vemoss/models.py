from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


#usuario
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=55, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email,full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
                email,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


